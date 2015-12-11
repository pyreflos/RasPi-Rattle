# RasPi-Rattle
RASpberry PI - RemoTe Time LapsE: find wifi, plug in power, take pictures, make video, upload to the web

Copyright (c) 2015 Pyre Flos, Provided to the public under The MIT License

####What is it?

RasPi-Rattle is a time lapse photography project powered by a Raspberry Pi and the Raspberry Pi Camera Module. It is written in python and is designed to take high-resolution images, upload them to Dropbox, and combine the images into a video. It is intended to be a stand-alone process - once the hardware is assembled, the software installed, and the configuration checked, the complete package can be setup somewhere, powered on, and everything else is automated.

####How do I use it?

Please see the Installation Guide. ```Installation_Guide.md``` will take you through the entire installation process, start-to finish, and is written for someone with no knowledge of programming. To get started, grab the required hardware (see below), an internet connection, and NOOBS pre-installed on an SD Card (https://www.raspberrypi.org/downloads/noobs/).

####Current Status

In its current state, the software will auto-start at system boot, take full resolution images, and then upload said images to Dropbox. It also has a hardware shutdown button to safely shutdown the Raspberry Pi without the need of a keyboard, mouse, or display device. The hardware currently displays which subroutine is running, if an image is being taken, and if an image upload has just been completed.

Unfortunately, video processing has not yet been implemented.

####The Future

The intended future state of the project is to have two operating modes: a “civilized” mode and an “uncivilized” mode. The civilized version will require an internet connection, host a local sftp server, possible vpn tunneling, and process video on demand via ssh commands. This way the system truly is remotely controlled. The uncivilized version, which might be more aptly named the “lite” version, will be completely headless with no need for setup beyond installation & initial configuration. Everything will be controlled via a few hardware buttons, with start/stop for the time lapse, video processing, and Wi-Fi connection. Retrieving files will be via ssh/sftp again, but those services will only run on demand. It will also be designed to minimize power usage, so as to allow the whole system to run on battery power.

####Hardware:

Required and recommended hardware listed below. Circuit design for the Control Circuit is shown under Control_Circuit.png.

| Required Hardware | For Setup Only | Recommended Hardware | Optional Hardware |
| ----- | ----- | ----- | ----- |
| Raspberry Pi | Keyboard | Wifi Dongle | Display* |
| Raspberry Pi Camera | Mouse | RTC DS1307 | PaPirus** | 
| Control Circuit | Display |  |  |  |
| Power Supply (5v, 500+ mA) |  |  |  |
* *programming optimized for 7" IPS screen @ 1280x800, but can easily be modified via config.py
* **future implementation - this will replace the control circuit and RTC, and be an option in config.py

####Dependencies:

* Dropbox-Uploader by andreafabrizi  (https://github.com/andreafabrizi/Dropbox-Uploader)
* Picamera (https://github.com/waveform80/picamera)
* PaPirus (optional) (https://www.kickstarter.com/projects/pisupply/papirus-the-epaper-screen-hat-for-your-raspberry-p)

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

