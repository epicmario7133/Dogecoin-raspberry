import time
import sys
import json
import urllib.request
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

display = Adafruit_SSD1306.SSD1306_128_64(rst=None)


# download raw json object
url = "https://dogechain.info/api/v1/address/balance/DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

print("balance:" + obj["balance"])
#tutti i cazzi del display:
balance = obj["balance"]
title = "Ðogecoin"
by = "By EpicMario71"
text = "Balance:"

# Setup
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.load_default()  # load and set default font
draw.text((40,2), title, fill=655)
draw.text((40,25), text, fill=655)
draw.text((25,35), balance, fill=655)
draw.text((25,53), by, fill=655)
display.image(image)  # set display buffer with image buffer
display.display()  # write display buffer to physical display
# Cleanup
GPIO.cleanup()  # release all GPIO resources
