from flask import Flask, jsonify
import RPi.GPIO as GPIO

import pins as Pins

app = Flask(__name__)

pwr_state = False
start_state = False
hl_low_state = False
hl_high_state = False
turn_left_state = False
turn_right_state = False
pl_state = False
rev_state = False
br_state = False

Pins.setup()

@app.route('/api/')
def index():
    return jsonify({
                    'pwr': pwr_state, 'start': start_state,
                    'hl_low': hl_low_state, 'hl_high': hl_high_state,
                    'turn_left': turn_left_state, 'turn_right': turn_right_state,
                    'pl': pl_state, 'rev': rev_state, 'br': br_state
                  })

# power to the electronics, controllable and observable
@app.route('/api/power')
@app.route('/api/power/<req>')
def power(req = None):
    global pwr_state

    if req is not None:
        if req == 'on':
            pwr_state = True
        elif req == 'off':
            pwr_state = False

        GPIO.output(Pins.PWR, GPIO.LOW if pwr_state == False else GPIO.HIGH)

    return jsonify({ 'pwr': pwr_state })

# starter motor, controllable and observable
@app.route('/api/starter')
@app.route('/api/starter/<req>')
def starter(req = None):
    global start_state

    if req is not None:
        if req == 'on':
            start_state = True
        elif req == 'off':
            start_state = False

        GPIO.output(Pins.START, GPIO.LOW if start_state == False else GPIO.HIGH)

    return jsonify({ 'start': start_state })

# head lamps can be controlled and observed in three states: low beam, high beam and off
@app.route('/api/headlamps')
@app.route('/api/headlamps/<req>')
def headlamps(req = None):
    global hl_low_state, hl_high_state

    if req is not None:
        if req == 'low':
            hl_low_state = True
            hl_high_state = False
        elif req == 'high':
            hl_low_state = False
            hl_high_state = True
        elif req == 'off':
            hl_low_state = False
            hl_high_state = False

        GPIO.output(Pins.HL_LOW, GPIO.LOW if hl_low_state == False else GPIO.HIGH)
        GPIO.output(Pins.HL_HIGH, GPIO.LOW if hl_high_state == False else GPIO.HIGH)

    return jsonify({ 'hl_low': hl_low_state, 'hl_high': hl_high_state })

# turn lamps can only be observed (controlled by arduino)
@app.route('/api/turnlamps')
def turnlamps():
    global turn_left_state, turn_right_state
    turn_left_state = GPIO.input(Pins.TURN_LEFT_IN)
    turn_right_state = GPIO.input(Pins.TURN_RIGHT_IN)

    return jsonify({ 'turn_left': turn_left_state, 'turn_right': turn_right_state })

# parking lamps can be controlled and observed
@app.route('/api/parkinglamps')
@app.route('/api/api/parkinglamps/<req>')
def parkinglamps(req = None):
    global pl_state
    if req == 'on':
        pl_state = True
    elif req == 'off':
        pl_state = False

    if req is not None:
        GPIO.output(Pins.PL, GPIO.LOW if pl_state == False else GPIO.HIGH)

    return jsonify({ 'pl': pl_state })

# reverse can only be observed (lamps controlled by arduino)
@app.route('/api/reverse')
def reverse():
    global rev_state
    rev_state = GPIO.input(Pins.REV_IN)

    return jsonify({ 'rev': rev_state })

# brakes can only be observed (lamps controlled by arduino)
@app.route('/api/brakes')
def brakes():
    global br_state
    br_state = GPIO.input(Pins.BR_IN)

    return jsonify({ 'br': br_state })

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
