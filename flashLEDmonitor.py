#!/usr/bin/python

import RPi.GPIO as GPIO  
import time
import signal
import sys

GPIO.setmode(GPIO.BCM) 

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

GPIOmap = {
 6: "cog0",
 12: "cog1",
 13: "cog2",
 18: "cog3",
 19: "cog4",
 20: "cog5",
 21: "cog6",
 23: "cog7"
}

# Interrup handlers
###################
# Control-C handler (or kill -SIGINT)
def controlC_handler(sig, frame):
    print('SIGINT received, terminating...')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, controlC_handler)


def gpio_rising (channel):  
    time.sleep(.1)
    HiLo = GPIO.input(channel)
    print "Current pattern: " \
           + str(GPIO.input(23)) \
           + str(GPIO.input(21)) \
           + str(GPIO.input(20)) \
           + str(GPIO.input(19)) \
           + str(GPIO.input(18)) \
           + str(GPIO.input(13)) \
           + str(GPIO.input(12)) \
           + str(GPIO.input(6)) \

    if HiLo == 1:
       print GPIOmap[channel] + " online"
    elif HiLo == 0:
       print GPIOmap[channel] + " offline"
    else:
       print "GPIO state change unknown"


GPIO.add_event_detect(6, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(12, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(13, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(18, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(19, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(20, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(21, GPIO.BOTH, callback=gpio_rising)  
GPIO.add_event_detect(23, GPIO.BOTH, callback=gpio_rising)  
  
# Main program loop
###################
def main():
    print "Starting pattern: " \
           + str(GPIO.input(23)) \
           + str(GPIO.input(21)) \
           + str(GPIO.input(20)) \
           + str(GPIO.input(19)) \
           + str(GPIO.input(18)) \
           + str(GPIO.input(13)) \
           + str(GPIO.input(12)) \
           + str(GPIO.input(6)) \

    print "Waiting for edges on ports"
    while True:
      pass

if __name__ == "__main__":
  main()

