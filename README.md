# RasPi-Rattle
RASpberry PI - RemoTe Time LapsE: find wifi, plug in power, take pictures, make video, upload to the web

Copyright (c) 2015 Pyre Flos, Provided to the public under The MIT License

####Hardware:

Required and recommended hardware listed below. Circuit design for the Control Circuit is shown under Control_Circuit.png.

| Required Hardware | Recommended Hardware | Optional Hardware |
| ----- | ----- | ----- |
| Raspberry Pi | Wifi Dongle | Screen* |
| Raspberry Pi Camera | RTC DS1307 | PaPirus** | 
| Control Circuit |  |  |  |
| Power Supply (5v, 500+ mA) |  |  |
* *programming optimized for 7" IPS screen @ 1280x800, but can easily be modified via config.py
* **future implimentation - this will replace the control circuit and RTC, and be an option in config.py

####Dependencies:

Dropbox-Uploader by andreafabrizi  (https://github.com/andreafabrizi/Dropbox-Uploader)

Picamera

PaPirus (optional)

####Image Options

| Option | Name | Image Size | Aspect Ratio| Video Processing |
| :-----: | :-----: | :-----: | :-----: | ----- |
| 0 | Custom | size set by user | n/a | same as image |
| 1 | Full Size | 2592x1944 | 4:3 | same as image |
| 2 | DCI 2k | 2592x1367* | 19:10 | scale to 2048x1080 |
| 3* | 1080p | 2592x1458* | 16:9 | scale to 1920x1080 |
| 4 | 720p | 2592x1458* | 16:9 | scale to 1280x720 |
* *Top/Bottom of camera output cropped equally
* ** This is the default

