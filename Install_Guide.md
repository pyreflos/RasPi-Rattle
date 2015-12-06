#How to Install and Use RasPi-Rattle

###Initial Setup

Grab your hardware and plug it all together, EXCEPT the wifi dongle. (Don't forget a keyboard, mouse, and monitor for the initial setup.)

Grab a fresh SD Card and install NOOBS (https://www.raspberrypi.org/help/noobs-setup/)

###Installing Dependencies

Shut down your Pi and plug in the wifi dongle.

Now restart the Pi, find your local wireless network and connect.

Update you baseline software and hardware by opening a terminal window and typing:

    sudo apt-get update
    sudo apt-get upgrade

Make sure python is installed (They should be pre-installed on Jessie):

    sudo apt-get install python-pip python3-pip python-picamera python3-picamera python-rpi.gpio python3-rpi.gpio

Make sure python camera software is installed (again, this should be pre-installed):

    sudo apt-get install python-picamera
    
Install tools for compiling images into video:

    sudo apt-get -y install libav-tools

Install GPIO support (Python Development first, then the GPIO itself)

    sudo apt-get install python-dev
    sudo apt-get install python-rpi.gpio
    
Install i2c support:

    sudo apt-get install python-smbus
    sudo apt-get install i2c-tools

Now verify the i2c installed correctly:

    sudo nano /etc/modules
    
and add these two lines to the end of the file if they aren't there:

    i2c-bcm2708 
    i2c-dev

If you are running a recent Raspberry Pi (3.18 kernel or higher) you will also need to update the /boot/config.txt file. Edit it with:

    sudo nano /boot/config.txt

and add the text

    dtparam=i2c1=on
    dtparam=i2c_arm=on

Once this is all done, reboot!
    sudo reboot

Then test i2c for the later model Pi's with:

    sudo i2cdetect -y 1

and the earlier ones with:

    sudo i2cdetect -y 0

Install the Real Time Clock:

First, load up the RTC module by running

    sudo modprobe rtc-ds1307
    
Then, as root (type in sudo bash) run
```echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device``` (if you have a rev 1 Pi)
```echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device``` (if you have a rev 2 Pi)
    
You can then type in "exit" to drop out of the root shell.
Once the time is correct (check with the date command), run ```sudo hwclock -w``` to write the system time to the RTC

You can then verify it with ```sudo hwclock -r```
Run ```sudo nano /etc/modules``` and add rtc-ds1307

Then you'll want to create the DS1307 device creation at boot, edit /etc/rc.local by running
```sudo nano /etc/rc.local```
and add:
```echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-0/new_device``` (for v1 raspberry pi)
```echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device``` (v2 raspberry pi)
```sudo hwclock -s``` (both versions)
before exit 0





