import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

x = False
while 1:
    x = ~x
    if x:
        GPIO.output(14, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(15, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(18, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(23, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(24, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(25, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(8, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(7, GPIO.HIGH)
        sleep(0.5)
    else:
        GPIO.output(14, GPIO.LOW)
        sleep(0.5)
        GPIO.output(15, GPIO.LOW)
        sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        sleep(0.5)
        GPIO.output(23, GPIO.LOW)
        sleep(0.5)
        GPIO.output(24, GPIO.LOW)
        sleep(0.5)
        GPIO.output(25, GPIO.LOW)
        sleep(0.5)
        GPIO.output(8, GPIO.LOW)
        sleep(0.5)
        GPIO.output(7, GPIO.LOW)
        sleep(0.5)
