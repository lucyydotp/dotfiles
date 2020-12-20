#!/usr/bin/env python
from i3ipc import Connection, Event
from colored import fg, attr

i3 = Connection()

def generate(self, _):
    out = "\n"
    for container in i3.get_tree().find_focused().workspace():
        try:
            if container.focused:
                out += fg("white") + attr("underlined") + container.name + attr("reset")
            else:
                out += container.name
            out += fg("#545454") + " | " + attr("reset")
        except Exception:
            pass
    out = out[:-18]
    print(out, end = '')

i3.on(Event.WINDOW_NEW, generate)
i3.on(Event.WINDOW_FOCUS, generate)

i3.main()
