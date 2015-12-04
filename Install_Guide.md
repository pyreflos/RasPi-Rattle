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


