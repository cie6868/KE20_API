#
#   Pin definitions for KE20 control.
#   Use BCM numbering.
#

import RPi.GPIO as GPIO

# outputs (relays)
PWR             =   14  # ignition/power
START           =   15  # starter motor
HL_LOW          =   18  # low beam
HL_HIGH         =   23  # high beam
PL              =   24  # parking lamps

# inputs
TURN_LEFT_IN    =   11
TURN_RIGHT_IN   =   9
REV_IN          =   10  # reverse
BR_IN           =   22  # brakes

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PWR, GPIO.OUT);
    GPIO.setup(START, GPIO.OUT);
    GPIO.setup(HL_LOW, GPIO.OUT);
    GPIO.setup(HL_HIGH, GPIO.OUT);
    GPIO.setup(PL, GPIO.OUT);

    GPIO.setup(TURN_LEFT_IN, GPIO.IN);
    GPIO.setup(TURN_RIGHT_IN, GPIO.IN);
    GPIO.setup(REV_IN, GPIO.IN);
