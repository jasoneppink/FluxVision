#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from evdev import uinput, ecodes as e

def skip_video(channel):
        with uinput.UInput() as ui:
                ui.write(e.EV_KEY, e.KEY_O, 1)
                ui.syn()

#define skip button GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pin 40
GPIO.add_event_detect(21, GPIO.FALLING, callback=skip_video, bouncetime=500)

while True:
	keep_alive = True
