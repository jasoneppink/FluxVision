#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from evdev import uinput, ecodes as e
import time
import subprocess, signal
from subprocess import check_output
import os

#define skip button GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pin 40

#define LED GPIO pin
GPIO.setup(13, GPIO.OUT) #pin 33
GPIO.output(13, True)

count = 0
prev_inp = 1

def skip_video(PinNr):
	global prev_inp
	global count

	inp = GPIO.input(PinNr)
	if ((not prev_inp) and inp):
		count = count + 1

		#turn off LED
		GPIO.output(13,False)

		#print "o", which tells omxplayer to skip to the next video
		with uinput.UInput() as ui:
			ui.write(e.EV_KEY, e.KEY_O, 1)
			ui.syn()

		#kill ticker.py (multiple instances if necessary)
		pids = check_output(["pgrep","-f","ticker.py"])
		for pid in pids.splitlines():
			try:
				os.kill(int(pid), signal.SIGKILL)
			except Exception,exc:
				print str(exc)

		#relaunch ticker.py
		subprocess.Popen("/home/pi/ticker.py &", shell=True)

		#disble button for 1 second
		time.sleep(1.0)

		#turn on LED
		GPIO.output(13,True)

	prev_inp = inp

try:
	while True:
		skip_video(21)
except KeyboardInterrupt:
	GPIO.cleanup()
