#!/usr/bin/env python
# THIS FILE SHOULD NOT BE IN LUCYY-MC/DOTFILES-NEW

import json
import socket
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
from time import sleep
from tabulate import tabulate

socket.setdefaulttimeout(2)
def _byte(b):
    return bytes((b, ))

def to_varint(number):
    buf = b''
    while True:
        towrite = number & 0x7f
        number >>= 7
        if number:
            buf += _byte(towrite | 0x80)
        else:
            buf += _byte(towrite)
            break
    return buf

def from_varint(stream):
    shift = 0
    result = 0
    while True:
        i = stream.recv(1)[0]
        result |= (i & 0x7f) << shift
        shift += 7
        if not (i & 0x80):
            break

    return result

def readall(stream, count):
    buf = b''
    for x in range(0, count):
        buf += stream.recv(1)
    return buf

def generate_handshake(server, port, next_state, proto=754):
    handshake = b'\x00'
    handshake += to_varint(proto)
    handshake += len(server).to_bytes(1, 'big')
    handshake += server.encode()
    handshake += port.to_bytes(2, 'big')
    handshake += next_state
    return len(handshake).to_bytes(1, 'big') + handshake



def get_all_data(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.sendall(generate_handshake(server, port, b'\x01'))

    # request
    s.sendall(b'\x01\x00')
    
    from_varint(s)
    from_varint(s)

    data = readall(s, from_varint(s)).decode("utf-8",errors="ignore")
    json_data = json.loads(data)

    s.close()

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((server, port))
    if json_data["version"]["protocol"] == -1:
        json_data["auth"] == "Proto -1"
        return json_data

    s2.sendall(generate_handshake(server, port, b'\x02', json_data["version"]["protocol"]))
   
    s2.sendall(b'\x08\x00\x06pinger')
    from_varint(s2)
    next_packet = from_varint(s2)
   
    if next_packet == 1: json_data["auth"] = "Online"
    elif next_packet == 0:
        print("Error found:", end="")
        read_count = from_varint(s2)
        error = s2.recv(read_count)
        print(error)
        json_data["auth"] = "Err: " + parse_component(json.loads(error))

        if json_data["auth"].startswith("Err: If you wish to use IP forwarding"):
            json_data["auth"] = "IPF"
        elif "Forge" in json_data["auth"]:
            json_data["auth"] = "Forge"
    else: json_data["auth"] = "Offline" 
    return json_data


def parse_component(component):
    output = ""
    try:
        output = component["text"]
    except TypeError:
        output = component
    except KeyError:
        output = component["translate"]

    try:
        if len(component["extra"]) != 0:
            for x in range(0, len(component["extra"])):
                output += parse_component(component["extra"][x])
    except (KeyError, TypeError):
        pass
    return output

def get_range():
    ports = input("Range (leave blank for default): ")
    if ports == "":
        return "1024-50000"
    return ports

ip = input("IP: ")

nm = NmapProcess(ip, options="-np" + get_range())
nm.run_background()
while nm.is_running():
    print("Port scanning: ETC: {0} DONE: {1}%".format(nm.etc, nm.progress))
    sleep(1)

parsed = NmapParser.parse(nm.stdout)
open_ports = []
for srv in parsed.hosts[0].services:
    print("Port " + str(srv.port) + " " + srv.state)
    if srv.state == "open": open_ports.append(srv.port)

data = []

for port in open_ports:
    try:
        status = get_all_data(ip, port)
        try:
            desc = parse_component(status["description"])
        except TypeError:
            desc = ""
        print(desc)
        #status = print(f"Port {port}, v{status.version.protocol} {status.version.name}, {status.players.online} online, desc {desc}")
        data.append([port, status["version"]["protocol"], status["version"]["name"], status["players"]["online"],status["auth"],  desc])
    except (ConnectionRefusedError, OSError, KeyError, socket.timeout, IndexError, json.decoder.JSONDecodeError) as e:
        print(e)
print(tabulate(data, headers=["Port", "Ver.", "Software", "Players", "Auth", "MotD"]))
