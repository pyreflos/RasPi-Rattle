##  External Module import
import RPi.GPIO as GPIO
import time
import atexit

##  Pin Definition:
ledPinA = 17  ##  Physical (BCM) 37; GPIO 26
ledPinB = 18  ##
ledPinC = 27  ##
ledPinD = 22  ##
BtnPinA = 5  ##  Physical (BCM) 35; GPIO 19
BtnPinB = 6  ##
BtnPinC = 13  ##
BtnPinD = 19  ##

##  Pin Setup:
GPIO.setmode(GPIO.BCM)  ##  Broadcom pin-numbering scheme
GPIO.setup(ledPinA, GPIO.OUT)  ## LED pin set as output
GPIO.setup(ledPinB, GPIO.OUT)
GPIO.setup(ledPinC, GPIO.OUT)
GPIO.setup(ledPinD, GPIO.OUT)
GPIO.setup(BtnPinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)  ##  Button pin set as input w/ pull up
GPIO.setup(BtnPinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  ##
GPIO.setup(BtnPinC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  ##
GPIO.setup(BtnPinD, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  ##

##  Initial state for LEDs:
GPIO.output(ledPinA, GPIO.LOW)
GPIO.output(ledPinB, GPIO.LOW)
GPIO.output(ledPinC, GPIO.LOW)
GPIO.output(ledPinD, GPIO.LOW)

##  Initial machine states:
Atest = 0
Btest = 0
Ctest = 0
Dtest = 0

def cleanup():
    print('Ended abruptly')
    GPIO.cleanup()
atexit.register(cleanup)

def blink(pin):
    bi = 0
    while (bi < 9):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)
        bi = bi + 1
    return

def toggleA(channel):
    global Btest
    if (Atest == 0):
        GPIO.output(ledPinA, GPIO.HIGH)
        Atest = 1
    elif (Atest == 1):
        GPIO.output(ledPinA, GPIO.LOW)
        Atest = 0
    return

def toggleB(channel):
    global Btest
    if (Btest == 0):
        GPIO.output(ledPinB, GPIO.HIGH)
        Btest = 1
    elif (Btest == 1):
        GPIO.output(ledPinB, GPIO.LOW)
        Btest = 0
    return

def toggleC(channel):
    global Ctest
    if (Ctest == 0):
        GPIO.output(ledPinC, GPIO.HIGH)
        Ctest = 1
    elif (Ctest == 1):
        GPIO.output(ledPinC, GPIO.LOW)
        Ctest = 0
    return

def toggleD(channel):
    global Dtest
    if (Dtest == 0):
        GPIO.output(ledPinD, GPIO.HIGH)
        Dtest = 1
    elif (Dtest == 1):
        GPIO.output(ledPinD, GPIO.LOW)
        Dtest = 0
    return

GPIO.add_event_detect(BtnPinA, GPIO.FALLING, callback=toggleA, bouncetime=200)
GPIO.add_event_detect(BtnPinB, GPIO.FALLING, callback=toggleB, bouncetime=200)
GPIO.add_event_detect(BtnPinC, GPIO.FALLING, callback=toggleC, bouncetime=200)
GPIO.add_event_detect(BtnPinD, GPIO.FALLING, callback=toggleD, bouncetime=200)

GPIO.output(ledPinA, GPIO.HIGH)
GPIO.output(ledPinB, GPIO.HIGH)
GPIO.output(ledPinC, GPIO.HIGH)
GPIO.output(ledPinD, GPIO.HIGH)
time.sleep(2)
GPIO.output(ledPinA, GPIO.LOW)
GPIO.output(ledPinB, GPIO.LOW)
GPIO.output(ledPinC, GPIO.LOW)
GPIO.output(ledPinD, GPIO.LOW)


while True:
#    GPIO.wait_for_edge(BtnPinD, GPIO.FALLING)
#    time.sleep(0.2)
#    blink(ledPinD)
    print('program running')
    time.sleep(120)
