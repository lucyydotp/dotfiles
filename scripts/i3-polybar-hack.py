#!/usr/bin/env python
# ---
# Lucy's Dotfiles
# https://github.com/lucyy-mc/dotfiles
# ---
# 
# Sets gaps dynamically on the primary monitor
# This is needed because i3 is ~quirky~ and polybar cant do anything about it

import i3ipc
import time

# which display the bar is on
BAR_DISPLAY = "DP-1"

# the size of the gap to add
GAP_SIZE = 38

# give i3 a minute to sort itself out
time.sleep(.1)

i3 = i3ipc.Connection()

def on_ws(i3, e):
    if e.ipc_data["current"]["output"] == BAR_DISPLAY:
        i3.command(f"gaps top current set {GAP_SIZE}")
        print(f"Adjusting {e.current.num}")

i3.on(i3ipc.Event.WORKSPACE, on_ws)

for ws in i3.get_workspaces():
    if ws.output == BAR_DISPLAY:
        i3.command(f"workspace {ws.num}")
        i3.command(f"gaps top current set {GAP_SIZE}")
        print("Adjusting " + str(ws.num))

i3.main()
