#!/usr/bin/python
# -*- coding: utf-8 -*-
# TODO: detect simulated "o" key press (from skip button) and immediately display new title

# Based on AdaFruit example
import math
import time
import Adafruit_CharLCD as LCD
import os
import socket

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

# Raspberry Pi pin configuration:
lcd_rs        = 27
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Scroll function
def scroll(lcd, text):
	n = 0
	#if there are more than 16 characters in the title, scroll
	if len(text)>16:
		for i in range(0, len(text)-15):
			lcd.message("Now playing:\n" + text[n:n+16])
			n += 1
			# Pause longer on beginning and end of scroll
			if i==0 or i==len(text)-16:
				time.sleep(2)
			else:
				time.sleep(.5)
			lcd.clear()
	#if there are 16 or fewer characters, don't scroll
	else:
		lcd.message("Now playing:\n" + text)
		time.sleep(6.0)
		lcd.clear()

while True:
	if os.path.isfile(abs_path + '.title_txt') is True:
		with open(abs_path + '.title_txt') as titlefile:
			titledata = titlefile.read()
		#if titledata is an IP address
		try:
			socket.inet_aton(titledata)
			lcd.clear()
			lcd.message("IP Address:\n" + titledata)
			time.sleep(10.0)
			#lcd.clear()
			#lcd.message(" Downloading\n videos now...  ")
		#otherwise it's a title
		except socket.error:
			if titledata == "Acquiring IP\naddress...":
				lcd.clear()
				lcd.message(titledata)
				time.sleep(10.0)
			else:
				scroll(lcd, titledata)
				lcd.clear()
				lcd.message("You're watching\nFluxVision!")
				time.sleep(6.0)
				lcd.clear()
	else:
		lcd.message(" File Not Found")
		time.sleep(6.0)
		lcd.clear()
