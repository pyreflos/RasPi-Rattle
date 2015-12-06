##  External module imports
import RPi.GPIO as GPIO
import time
import os

##  Pin Definitions:
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)  ##  Physical (BCM) 12; GPIO 18

while True:
    if(GPIO.input(17) == False):
        os.system("sudo shutdown -h now")
        break
    time.sleep(1)
    
