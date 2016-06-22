#!/usr/bin/python
# Based on AdaFruit example
import math
import time
import Adafruit_CharLCD as LCD
import os

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"
print abs_path

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
	for i in range(0, len(text)-15):
		lcd.message("Now playing:\n" + text[n:n+16])
		n += 1
		# Pause longer on beginning and end of scroll
		if i==0 or i==len(text)-16:
			time.sleep(2)
		else:
			time.sleep(.5)
		lcd.clear()

while True:
	with open(abs_path + '.title_txt') as titlefile:
		titledata = titlefile.read()
	scroll(lcd, titledata)
	lcd.message("You're watching\nFluxVision!")
	time.sleep(6.0)
	lcd.clear()
