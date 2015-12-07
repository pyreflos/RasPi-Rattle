##  External module imports
import RPi.GPIO as GPIO
import time
import os
import atexit
import sys

##  Pin Definitions:
ledPower = 22  ##  BCM/GPIO 22; Physical pin 15
btnPower = 12  ##  BCM/GPIO 12; Physical pin 32

##  Pin Setup:
GPIO.setmode(GPIO.BCM) ## Broadcom pin-numbering scheme enabled
GPIO.setup(ledPower, GPIO.OUT) ## Power Off LED pin set as output
GPIO.setup(btnPower, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) ## Power Off button pin set as input w/ pull-up

##  Initial State for LEDs:
GPIO.output(ledPower, GPIO.HIGH)

## Variable setup:
panic = 0

##  Cleanup GPIO pins on exit
def cleanup():
  print('Ended abruptly')
  GPIO.cleanup()
atexit.register(cleanup)

##  Shut down Raspberry Pi after blinking LEDs
def killpi(channel):
    print('Shutting down Raspberry Pi now...')
    global panic
    panic = 1
    os.system("sudo shutdown -h now")
    time.sleep(1)

## Main program
GPIO.add_event_detect(btnPower, GPIO.FALLING, callback=killpi, bouncetime=200)

#while True:
while (panic == 0):
    GPIO.output (ledPower, GPIO.LOW)
    time.sleep (4.9)
    GPIO.output (ledPower, GPIO.HIGH)
    time.sleep (0.1)
##    print('Still on...')
else:
    while (panic == 1):
        GPIO.output (ledPower, GPIO.LOW)
        time.sleep (0.1)
        GPIO.output (ledPower, GPIO.HIGH)
        time.sleep (0.1)
##        print('die!')
    else:
        pass
