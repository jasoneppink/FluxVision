#!/usr/bin/python
# This script imports playlist.dat
# updates it in the background
# and plays each video
import sys
import subprocess
import os
import pickle
import get_youtube
from get_youtube import update
import thread
import time
from time import localtime, strftime

playlist_id = sys.argv[1]

#blank out the command line, mostly
#os.system('clear')
#subprocess.call(['printf', '%b\n', '\033[2J\033[:H'], stdout=open(os.devnull, 'wb'))

#get absolute path of this script (necessary because it's being called, indirectly, from rc.local)
abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

try:
	with open(abs_path + 'playlist.dat') as f:
		playlist = pickle.load(f)
except:
	playlist = []

#get_youtube.py function
thread.start_new_thread(update, (playlist_id,))

for video in playlist:
	#update title for ticker
	with open(abs_path + 'title.txt', 'w') as title:
		title.truncate()
		title.write(video.title)

	#adjust volume based on time (mute from 11pm to 10am)
	if int(strftime("%-H%M", localtime())) > 2300 or int(strftime("%-H%M", localtime())) < 1000:
		#mute audio
		vol=-6000
	else:
		vol=0

	#play video (but make sure it exists first)
	if os.path.isfile(abs_path + video.filename):
		process = subprocess.call(['omxplayer', '-b', '-o', 'local', abs_path + video.filename, '--vol', str(vol)], stdout=open(os.devnull, 'wb'))

	#test blank
#	os.system('clear')
#	subprocess.call(['printf', '%b\n', '\033[2J\033[:H'], stdout=open(os.devnull, 'wb'))
#	time.sleep(10)
