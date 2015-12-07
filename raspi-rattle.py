##  
##  RASpberry PI - RemoTe Time LapsE
##  
##  ===== =====   Version 0.1   ===== =====
##  
##  This is the first iteration and is really badly hacked together.
## 
##  Required hardware:
##      Raspberry Pi, Raspberry Pi Camera, Wifi Dongle
##
##  Dependencies:
##      Dropbox-Uploader by andreafabrizi (https://github.com/andreafabrizi/Dropbox-Uploader)
##  


##  External module imports
import RPi.GPIO as GPIO
import time
import picamera
from datetime import datetime, timedelta
from subprocess import call
import atexit

##  Pin Definitions:
LED_Prgm = 11  ##  Physical (BCM) 11; GPIO 17
LED_Image = 13  ##  Physical (BCM) 13; GPIO 27
LED_Video = 15  ##  Physical (BCM) 15; GPIO 22
Btn_Image = 29  ##  Physical (BCM) 29; GPIO 5
Btn_Video = 31  ##  Physical (BCM) 31; GPIO 6

##  Variables Setup:
file_path = '/home/pi/ZBA_Timelapse/images/'

##  Cleans GPIO pins on program exit
def cleanup():
    print('Ended abruptly')
    GPIO.cleanup()
atexit.register(cleanup)

def wait():
    # Calculate the delay to the start of the next hour
##    next_hour = (datetime.now() + timedelta(minute=1)).replace(
##        second=0, microsecond=0)
    next_hour = (datetime.now() + timedelta(minutes=1))
    delay = (next_hour - datetime.now()).seconds
    time.sleep(delay)
##    return

def remove_prefix(pathy, prefix):
    if pathy.startswith(prefix):
        return pathy[len(prefix):]
    return text
##    return pathy[pathy.startswith(prefix) and len(prefix):]

with picamera.PiCamera() as camera:
    camera.led = False
    camera.resolution = (2592, 1944)
    camera.start_preview()
    camera.preview.fullscreen = False
    camera.preview.alpha = 128
    camera.preview.window = (107, 0, 1066, 800)
##    time.sleep(60)
    wait()
 #   for filename in camera.capture_continuous('/home/pi/ZBA_Timelapse/images/img_{timestamp:%Y-%m-%d}_{timestamp:%H-%M-%S}.jpg'):
    for filename in camera.capture_continuous(file_path + 'img_{timestamp:%Y-%m-%d}_{timestamp:%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        filename_up = remove_prefix(filename, file_path)
 ##       filename_up = file_path + filename
        upload_file = ('/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload ' + file_path + filename_up + " " + filename_up)
        call ({upload_file}, shell=True)
        wait()
