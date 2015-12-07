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
LED_Prgm = 27 ## BCM/GPIO 27 - BOARD/Physical 13
LED_Upload = 18 ## BCM/GPIO 18 - BOARD/Physical 12
#LED_Video = 17 ## BCM/GPIO 17 - BOARD/Physical 11
#Btn_Image = 6 ## BCM/GPIO 6 - BOARD/Physical 31
#Btn_Video = 5 ## BCM/GPIO 5 - BOARD/Physical 29

##  Pin Setup:
GPIO.setmode(GPIO.BCM) ## Broadcom pin-numbering scheme
GPIO.setup(LED_Prgm, GPIO.OUT) ## LED pin set as output
GPIO.setup(LED_Upload, GPIO.OUT)
#GPIO.setup(LED_Video, GPIO.OUT)
#GPIO.setup(Btn_Image, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) ## Button pin set as input w/ pull up
#GPIO.setup(Btn_Video, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Not used... GPIO.setup(Btn3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

##  Initial state for LEDs:
GPIO.output(LED_Prgm, GPIO.HIGH)
GPIO.output(LED_Upload, GPIO.LOW)
#GPIO.output(LED_Video, GPIO.LOW)

##  Initial machine states & variables:
Prgm_State = 1
Image_State = 1
Video_State = 0
Image_State_Temp = 0
file_path = '/home/pi/ZBA_Timelapse/images/'
img_minute = 1 # time between images in minutes

##  Cleans GPIO pins on program exit
def cleanup():
    print('Ended abruptly')
    GPIO.cleanup()
atexit.register(cleanup)

def wait():
    # Calculate the delay to the start of the next hour
##    next_hour = (datetime.now() + timedelta(minute=1)).replace(
##        second=0, microsecond=0)
    global img_minute
    next_hour = (datetime.now() + timedelta(minutes=3)).replace(
      second=0, microsecond=0)
    delay = (next_hour - datetime.now()).seconds
    time.sleep(delay)
##    return

def upload_blink():
    GPIO.output(LED_Upload, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(LED_Upload, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(LED_Upload, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(LED_Upload, GPIO.LOW)
    time.sleep(0.25)

def remove_prefix(pathy, prefix):
    if pathy.startswith(prefix):
        return pathy[len(prefix):]
    return text
##    return pathy[pathy.startswith(prefix) and len(prefix):]

with picamera.PiCamera() as camera:
    camera.led = False
    camera.resolution = (2592, 1367) #max 2592,1944 - 2k 2048,1080
    camera.start_preview()
    camera.preview.fullscreen = False
    camera.preview.alpha = 128
    camera.preview.window = (107, 0, 1066, 800)
##    time.sleep(60)
    wait()
 #   for filename in camera.capture_continuous('/home/pi/ZBA_Timelapse/images/img_{timestamp:%Y-%m-%d}_{timestamp:%H-%M-%S}.jpg'):
    for filename in camera.capture_continuous(file_path + 'img_{timestamp:%Y%m%d%H%M%S}.jpg', resize=(2048,1080), quality=(95)):
        print('Captured %s' % filename)
 #       GPIO.output(LED_Upload, GPIO.HIGH
        filename_up = remove_prefix(filename, file_path)
 ##       filename_up = file_path + filename
        upload_file = ('/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload ' + file_path + filename_up + " " + filename_up)
        call ({upload_file}, shell=True)
        upload_blink()
#        GPIO.output(LED_Upload, GPIO.LOW)
        wait()
