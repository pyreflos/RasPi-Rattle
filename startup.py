import time
from threading
import os

def startprgm(i):
    print "Running thread %d" % i
    if (i == 0):
        time.sleep(1)
        print('Executing: shutdown.py')
        os.system("sudo python /home/pi/RasPi-Rattle/shutdown.py")
        print('Running: shutdown.py')
    elif (i == 1):
        print('Executing: raspi-rattle.py')
        time.sleep(1)
        os.system("sudo python /home/pi/RasPi-Rattle/raspi-rattle.py")
        print('Running: raspi-rattle.py')
    else:
        pass

for i in range(2):
    t = threading.Thread(target=startprgm, args=(i,))
    t.start()
