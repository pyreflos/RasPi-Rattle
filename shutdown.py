##  External module imports
import RPi.GPIO as GPIO
import time
import os
import atexit
import sys

##  Pin Definitions:
ledPower = 22  ##  BCM/GPIO 22; Physical pin 15
btnPower = 19  ##  BCM/GPIO 19; Physical pin 35

##  Pin Setup:
GPIO.setmode(GPIO.BCM)  ## Broadcom pin-numbering scheme enabled
GPIO.setup(ledPower, GPIO.OUT)  ## Power Off LED pin set as output
GPIO.setup(btnPower, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  ##  Power Off button pin set as input w/ pull-up

##  Initial State for LEDs:
GPIO.output(ledPower, GPIO.HIGH)

def cleanup():
  print('Ended abruptly')
  GPIO.cleanup()
atexit.register(cleanup)

while True:
    if(GPIO.input(btnPower, bouncetime=200) == False):
        sdi = 0
        while (count <9):
            GPIO.output (ledPower, GPIO.LOW)
            time.sleep (0.5)
            GPIO.output (ledPower, GPIO.HIGH)
            time.sleep (0.5)
            sdi = sdi + 1
        os.system("sudo shutdown -h now")
        GPIO.output (
        break
    time.sleep(1)
    
