#!/bin/bash

#clear screen
printf '%b\n' '\033[2J\033[:'
printf 'Acquiring IP address...'
printf 'Acquiring IP\naddress...' > /home/pi/.title_txt

#start video skip button
sudo /usr/bin/python /home/pi/skip_video.py &

#start ticker
sudo /usr/bin/python /home/pi/ticker.py &

sleep 30s

#print IP address
printf '%b\n' '\033[2J\033[:'
printf 'IP Address: '
ip route get 8.8.8.8 | awk '{print $7; exit}'
ip route get 8.8.8.8 | awk '{printf $7}' > /home/pi/.title_txt
sleep 10s

#clear screen again
printf '%b\n' '\033[2J\033[:'

#turn all prompt text black (keeps screen black)
sudo sh -c "TERM=linux setterm -foreground black >/dev/tty0"

#delete temporary files
rm -f /home/pi/.get_youtube_lck

#start video
while true
do
	/usr/bin/python /home/pi/play_youtube.py
done
