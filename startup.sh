#!/bin/bash

#make the command prompt have 0 characters
#bash --rcfile <(echo "PS1=''") -i

printf '%b\n' '\033[2J\033[:H'

while true
do
#	livestreamer --player-no-close new.livestream.com/accounts/13913910/events/4123403 288p --player omxplayer --fifo --player-args "--win \"0 0 800 480\" {filename}"
	/usr/bin/python /home/pi/play_youtube.py PLLV6BPSazQd4K5bGTy9oJxB3tCKLChVkH
done
