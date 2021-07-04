#!/usr/bin/env python
# ---
# Lucy's Dotfiles
# https://github.com/lucyy-mc/dotfiles
# ---
# 
# Sets gaps dynamically on the primary monitor
# This is needed because i3 is ~quirky~ and polybar cant do anything about it

import i3ipc

# which display the bar is on
BAR_DISPLAY = "DP-1"

# the size of the gap to add
GAP_SIZE = 38

i3 = i3ipc.Connection()

def on_ws(i3, e):
    if e.ipc_data["current"]["output"] == BAR_DISPLAY:
        i3.command("gaps top current plus " + str(GAP_SIZE))
        print(e.current.gaps)


i3.on(i3ipc.Event.WORKSPACE_INIT, on_ws)

for ws in i3.get_workspaces():
    if ws.output == BAR_DISPLAY:
        i3.command("gaps top current set " + str(GAP_SIZE))

i3.main()
