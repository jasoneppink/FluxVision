#!/usr/bin/python
# This script imports playlist.dat
# updates it in the background
# and plays each video
import sys
import subprocess
import os
import pickle
import threading
import time
from time import localtime, strftime
import ConfigParser

#get absolute path of this script (necessary because it's being called, indirectly, from rc.local)
abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

config = ConfigParser.ConfigParser()
config.readfp(open(abs_path + 'config.txt', 'r'))
playlist_id = config.get('FluxVision Config', 'playlist_id')
mute_night_time = config.get('FluxVision Config', 'mute_night_time')
unmute_morning_time = config.get('FluxVision Config', 'unmute_morning_time')
use_ticker = config.get('FluxVision Config', 'use_ticker')

class videoinfo(object):
        def __init__(self, title, youtubeURL, filename):
                self.title = title
                self.youtubeURL = youtubeURL
                self.filename = filename

#open .playlist_dat
try:
	with open(abs_path + '.playlist_dat') as f:
		playlist = pickle.load(f)
except Exception, e:
	playlist = []

for video in playlist:
	#update title for ticker
	if use_ticker == 'y':
		with open(abs_path + '.title_txt', 'w') as title:
			title.truncate()
			title.write(video.title)

	#adjust volume based on times in config.txt
	if int(strftime("%-H%M", localtime())) > int(mute_night_time) or int(strftime("%-H%M", localtime())) < int(unmute_morning_time):
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
