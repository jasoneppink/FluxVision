#!/bin/bash

#clear screen
printf '%b\n' '\033[2J\033[:'
printf 'acquiring IP address...'
sleep 30s

#print IP address
printf '%b\n' '\033[2J\033[:'
printf 'IP address: '
ip route get 8.8.8.8 | awk '{print $NF; exit}'
sleep 10s

#clear screen again
printf '%b\n' '\033[2J\033[:'

#turn all prompt text black (keeps screen black)
sudo sh -c "TERM=linux setterm -foreground black >/dev/tty0"

#delete temporary files
rm -f /home/pi/.get_youtube_lck
rm -f /home/pi/.title_txt

#start ticker
sudo /usr/bin/python /home/pi/ticker.py &

#start video
while true
do
	/usr/bin/python /home/pi/play_youtube.py
done
