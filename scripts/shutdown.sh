#!/bin/bash

# get rofi input

ACTION=$(echo -e "Shutdown\nReboot\nLogoff" | rofi -dmenu -p "power")

if [[ $ACTION == "Shutdown" ]] ;
	then systemctl poweroff
elif [[ $ACTION == "Reboot" ]] ;
	then systemctl reboot
elif [[ $ACTION == "Logoff" ]] ;
	then i3-msg exit
fi
