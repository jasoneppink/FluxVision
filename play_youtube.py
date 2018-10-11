#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script imports playlist.dat
# updates it in the background
# and plays each video
import sys, subprocess, signal, os, pickle, threading, time, ConfigParser
from subprocess import check_output
from time import localtime, strftime
from dashboard import update

#get absolute path of this script (necessary because it's being called, indirectly, from rc.local)
abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

#read from configuration file
config = ConfigParser.ConfigParser()
config.readfp(open(abs_path + 'config.txt', 'r'))
playlist_id = config.get('FluxVision Config', 'playlist_id')
mute_time = config.get('FluxVision Config', 'mute_time')
unmute_time = config.get('FluxVision Config', 'unmute_time')
default_volume = config.get('FluxVision Config', 'default_volume')
dashboard = config.get('FluxVision Config', 'dashboard')
use_ticker = config.get('FluxVision Config', 'use_ticker')


class videoinfo(object):
        def __init__(self, title, youtubeID, filename):
                self.title = title
                self.youtubeID = youtubeID
                self.filename = filename

#open playlist file
try:
	with open(abs_path + '.playlist_dat') as f:
		playlist = pickle.load(f)
except Exception, e:
	playlist = []

#open blacklist.txt file
try:
	with open(abs_path + 'blacklist.txt') as f:
		blacklist = f.readlines()
except Exception, e:
	blacklist = []

for video in playlist:
    #skip video if the title contains a line in blacklist.txt
    skipVideo = False
    for line in blacklist:
        if line[:-1] in video.title:
            skipVideo = True
            break
    if skipVideo:
        continue
    
	#adjust volume based on times in config.txt
	if (int(mute_time) > int(unmute_time)): # if mute happens before midnight
		if int(strftime("%-H%M", localtime())) > int(mute_time) or int(strftime("%-H%M", localtime())) < int(unmute_time):
			#mute
			vol = -6000
		else:
			vol = default_volume
	else: # if mute happens after midnight
		if int(strftime("%-H%M", localtime())) > int(mute_time) and int(strftime("%-H%M", localtime())) < int(unmute_time):
			vol = -6000
		else:
			vol = default_volume

	#if video file exists
	if os.path.isfile(abs_path + video.filename):
		#update .count_video
		with open(abs_path + '.count_video') as count_video:
			value = int(count_video.read())
		with open(abs_path + '.count_video', 'w') as count_video:
			count_video.write(str(value + 1))
		#update .title_txt
		with open(abs_path + '.title_txt', 'w') as title:
			title.truncate()
			title.write(video.title)
		#update /etd/motd (displays current video on login)
		if dashboard == 'y':
			update(video.title)
		#update ticker
		if use_ticker == 'y':
			#kill ticker.py (multiple instances if necessary)
			pids = check_output(["pgrep","-f","ticker.py"])
			for pid in pids.splitlines():
				try:
					os.system("sudo kill %d"%(int(pid)))
				except Exception,exc:
					print str(exc)
			#relaunch ticker.py
			try:
				subprocess.Popen("sudo python /home/pi/ticker.py &", shell=True)
			except Exception,exc:
				print str(exc)
		#play video
		process = subprocess.call(['omxplayer', '-b', '-o', 'local', abs_path + video.filename, '--vol', str(vol), '--no-osd'], stdout=open(os.devnull, 'wb'))

#increment .count_playlist
with open(abs_path + '.count_playlist') as count_playlist:
	value = int(count_playlist.read())
with open(abs_path + '.count_playlist', 'w' ) as count_playlist:
	count_playlist.write(str(value + 1))

#check if the playlist is currently being updated; if not, do that now as a separate process
if os.path.exists(abs_path + '.get_youtube_lck') is False:
	p = subprocess.Popen([sys.executable, abs_path + 'get_youtube.py'])
