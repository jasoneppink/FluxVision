#!/bin/bash

#printf '%b\n' '\033[2J\033[:H'

#delete temporary files
rm -f /home/pi/.get_youtube_lck
rm -f /home/pi/.title_txt

while true
do
#	livestreamer --player-no-close new.livestream.com/accounts/13913910/events/4123403 288p --player omxplayer --fifo --player-args "--win \"0 0 800 480\" {filename}"
	/usr/bin/python /home/pi/play_youtube.py
done
