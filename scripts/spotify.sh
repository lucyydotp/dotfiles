STATUS=$(playerctl -p spotify status 2>&1)

if [[ $STATUS == "No players found" ]] ;
then exit
elif [[ $STATUS == "Paused" ]] ;
then echo "Paused"
elif [[ $STATUS == "Playing" ]];
then
	echo $(playerctl -p spotify metadata artist) - $(playerctl -p spotify metadata title)
fi
