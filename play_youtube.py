#!/usr/bin/python
# This script imports playlist.dat
# updates it in the background
# and plays each video
import sys
import subprocess
import os
import pickle
#from get_youtube import videoinfo
#from get_youtube import update
import threading
import time
from time import localtime, strftime

playlist_id = sys.argv[1]

class videoinfo(object):
        def __init__(self, title, youtubeURL, filename):
                self.title = title
                self.youtubeURL = youtubeURL
                self.filename = filename

#get absolute path of this script (necessary because it's being called, indirectly, from rc.local)
abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

try:
	with open(abs_path + '.playlist_dat') as f:
		playlist = pickle.load(f)
except Exception, e:
#	print str(e)
	playlist = []

for video in playlist:
	#print "video: " + video.title

	#update title for ticker
	with open(abs_path + '.title_txt', 'w') as title:
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

#check if the playlist is currently being updated; if not, do that now as a separate process
if os.path.exists(abs_path + '.get_youtube_lck') is False:
	p = subprocess.Popen([sys.executable, abs_path + 'get_youtube.py'])
