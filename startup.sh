#!/bin/bash

#clear screen
printf '%b\n' '\033[2J\033[:'
printf 'Acquiring IP address...'
printf 'Acquiring IP\naddress...' > ${BASH_SOURCE%/*}/.title_txt

#start video skip button (uncomment this line if you are using a skip button)
#sudo /usr/bin/python ${BASH_SOURCE%/*}/skip_video.py &

#start ticker (uncomment this line if you are using a ticker)
#sudo /usr/bin/python ${BASH_SOURCE%/*}/ticker.py &

sleep 30s

#print IP address
printf '%b\n' '\033[2J\033[:'
printf 'IP Address: '
ip route get 8.8.8.8 | awk '{print $7; exit}'
ip route get 8.8.8.8 | awk '{printf $7}' > ${BASH_SOURCE%/*}/.title_txt
sleep 10s

#clear screen again
printf '%b\n' '\033[2J\033[:'

#turn all prompt text black (keeps screen black)
sudo sh -c "TERM=linux setterm -foreground black >/dev/tty0"

#reset temporary files
rm -f ${BASH_SOURCE%/*}/.get_youtube_lck
printf "0" > ${BASH_SOURCE%/*}/.count_video
printf "0" > ${BASH_SOURCE%/*}/.count_playlist

#start volume knob (uncomment this line if you are using a volume knob)
#sudo /usr/bin/python ${BASH_SOURCE%/*}/volume.py &

#start video playback
while true
do
	/usr/bin/python ${BASH_SOURCE%/*}/play_youtube.py
done
