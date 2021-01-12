#!/bin/bash

EVENING_THRESH=15
NIGHT_THRESH=18
while true 
do
	HOUR=$(date +%k)
	if [[ $HOUR > $NIGHT_THRESH ]];
	then
		WALLPAPER=night
	elif [[ $HOUR > $EVENING_THRESH ]];
	then
		WALLPAPER=evening	
	else
		WALLPAPER=day
	fi

	printf "Setting wallpaper to %s" $WALLPAPER
	feh --bg-fill ~/wallpaper/$WALLPAPER.png
	sleep 900
done
