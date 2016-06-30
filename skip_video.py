#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from evdev import uinput, ecodes as e
import time
import subprocess, signal
import os

def skip_video(channel):
	GPIO.output(13,False)
        with uinput.UInput() as ui:
                ui.write(e.EV_KEY, e.KEY_O, 1)
                ui.syn()
	#kill ticker.py
	p = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
	out, err = p.communicate()
	for line in out.splitlines():
		if 'ticker.py' in line:
			pid = int(line.split(None, 1)[0])
			print "ticker.py found! pid: " + str(pid)
			os.kill(pid, signal.SIGKILL)
	subprocess.Popen("/home/pi/ticker.py", shell=True)
	GPIO.output(13,True)

#define skip button GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pin 40
GPIO.add_event_detect(21, GPIO.FALLING, callback=skip_video, bouncetime=500)

#define LED GPIO pin
GPIO.setup(13, GPIO.OUT) #pin 33
GPIO.output(13, True)

while True:
	keep_alive = True
