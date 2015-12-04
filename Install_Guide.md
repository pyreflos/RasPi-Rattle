#How to Install and Use RasPi-Rattle

###Initial Setup

Grab all you hardware and plug it together, (EXCEPT the wifi dongle). Don't forget a keyboard, mouse, and monitor for the initial setup.

Grab a fresh SD Card and install NOOBS (https://www.raspberrypi.org/help/noobs-setup/)

###Installing Dependencies

Shut down your Pi and plug in the wifi dongle.

Now restart the Pi, find your local wireless network and connect.

Update you baseline software and hardware by opening a terminal window and typing:

    sudo apt-get update
    sudo apt-get upgrade

Make sure python is installed:

    sudo apt-get install python-camera python3-camera python-pip
