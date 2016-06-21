#!/usr/bin/python
# This script downloads information for each video in a YouTube playlist,
# downloads any videos it doesn't already have,
# and deletes any videos that are no longer in the playlist,
# then saves the list as playlist.dat for use with play_youtube.py

import subprocess
import collections
import os
import pickle

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

class videoinfo(object):
	def __init__(self, title, youtubeURL, filename):
		self.title = title
		self.youtubeURL = youtubeURL
		self.filename = filename

def update(playlist_id):
	#for each video in playlist, get title, YouTube URL, and (aspirational) local file name (media/ID.mp4)
	#'-f 18' is a 360p mp4 file (very standard option), others are mp4 backups with similar sizes
	raw_output = subprocess.check_output(['youtube-dl', '-o', "media/%(id)s.%(ext)s", 'https://www.youtube.com/playlist?list=' + playlist_id, '-f', '18/134/135/22', '--get-filename', '--get-title', '--get-url'])
	youtube_data = raw_output.splitlines()

	#parse into readable list of classes
	playlist = []
	i=0
	while i < len(youtube_data):
		print(youtube_data[i])
		playlist.append(videoinfo(youtube_data[i], youtube_data[i+1], youtube_data[i+2]))
		i += 3

	#if there's a video in the list that isn't already saved, download it
	for video in playlist:
		if os.path.isfile(abs_path + video.filename) is False:
			subprocess.check_output(['youtube-dl', '-o', abs_path + video.filename, video.youtubeURL])

	#if there's a video that has been previously saved that is no longer on the list, delete it
	for file in os.listdir(abs_path + "media"):
		match = False
		for video in playlist:
			if abs_path + video.filename == abs_path + "media/" + file:
				match = True
		if match is False:
			os.remove(abs_path + "media/" + file)

	#save the list of classes so play_youtube.py can use it
	with open(abs_path + "playlist.dat", "wb") as f:
		pickle.dump(playlist, f)
