# Dogecoin-raspberry
Dogecoin balance on 0.96 I2C Display On Raspberry

![IMG_20200603_183639](https://user-images.githubusercontent.com/56398081/83664464-523e1a80-a5ca-11ea-8956-3ba3a7b7ad34.jpg)

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

Now do:

git clone https://github.com/epicmario7133/Dogecoin-raspberry

cd Dogecoin-raspberry

nano dogescreen.py

go: url = "https://dogechain.info/api/v1/address/balance/DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx" and edit dis url whit our wallet example:

"https://dogechain.info/api/v1/address/balance/your-belance"

ctrl + x, press s, enter

now do:

watch -n 30 python3.7 dogescreen.py

If don't work check if url is correct and check the ""

or

Pin is not badly connected

or the display is not a 128x64 Pixel I2C

Do donation whit doge:

DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx

![DQax3WxFFPa5b5YmmwzJnek7Yknx3GFgsx](https://user-images.githubusercontent.com/56398081/83665414-b01f3200-a5cb-11ea-8a15-4a424647f937.png)
