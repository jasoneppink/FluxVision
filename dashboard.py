#!/usr/bin/python
# -*- coding: utf-8 -*-

# light modification of a script by Daniel G
# https://stackoverflow.com/questions/2598145/how-to-retrieve-the-process-start-time-or-uptime-in-python

def get_start_time():
	import os, sys, datetime, time, subprocess
	pid = str(int(subprocess.check_output(["pgrep","-of","startup.sh"])))

	proc = subprocess.Popen(['ps','-eo','pid,etime'], stdout=subprocess.PIPE)
	# get data from stdout
	proc.wait()
	results = proc.stdout.readlines()
	# parse data (should only be one)
	for result in results:
		try:
			result.strip()
			if result.split()[0] == pid:
				pidInfo = result.split()[1]
				# stop after the first one we find
				break
		except IndexError:
			pass # ignore it
	else:
		print "Process PID", pid, "doesn't seem to exist!"
		sys.exit(0)
	pidInfo = [result.split()[1] for result in results
		if result.split()[0] == pid][0]
	pidInfo = pidInfo.partition("-")
	if pidInfo[1] == '-':
		# there is a day
		days = int(pidInfo[0])
		rest = pidInfo[2].split(":")
		hours = int(rest[0])
		minutes = int(rest[1])
		seconds = int(rest[2])
	else:
		days = 0
		rest = pidInfo[0].split(":")
		if len(rest) == 3:
			hours = int(rest[0])
			minutes = int(rest[1])
			seconds = int(rest[2])
		elif len(rest) == 2:
			hours = 0
			minutes = int(rest[0])
			seconds = int(rest[1])
		else:
			hours = 0
			minutes = 0
			seconds = int(rest[0])

	# get the start time
	secondsSinceStart = days*24*3600 + hours*3600 + minutes*60 + seconds
	# unix time (in seconds) of start
	startTime = time.time() - secondsSinceStart
	# final result
	return datetime.datetime.fromtimestamp(startTime).strftime("%A %B %e at %l:%M %p")
