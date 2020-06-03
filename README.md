# Dogecoin-raspberry
Dogecoin belance on 0.96 I2C Display On Raspberry

First of all you have to install these packages with these commands:

sudo apt-get update
sudo apt-get install pip3
sudo apt-get install python3.7 
sudo apt-get install git
sudo pip3 install time
sudo pip3 install sys
sudo pip3 install json
sudo pip3 install urllib.request
sudo pip3 install Adafruit_SSD1306


Now do:
sudo raspi-config
Interfacecing Options > I2C > yes > exit

Now do connect the display


![Screenshot (27)](https://user-images.githubusercontent.com/56398081/83659742-3afc2e80-a5c4-11ea-85d1-52eb2173f6dd.png)

GND>GND
VNC>3.3V
SLC>GPIO.3
SDA>GPIO.2

![dzEcU](https://user-images.githubusercontent.com/56398081/83660161-cb3a7380-a5c4-11ea-9008-69f2c7b5c290.png)



