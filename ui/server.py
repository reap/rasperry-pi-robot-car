from flask import Flask
from flask import render_template
import GPIOEmu as GPIO
# import RPi.GPIO as GPIO
import time

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/move/forward")
def forward():
    run_forward()
    return "OK"


@app.route("/move/left")
def left():
    turn_left()
    return "OK"


@app.route("/move/right")
def right():
    turn_right()
    return "OK"


@app.route("/move/backward")
def backward():
    run_reverse()
    return "OK"


@app.route("/stop")
def stop():
    stop_running()
    return "OK"


PinRightMotorsForward = 38
PinRightMotorsBackward = 40


PinLeftMotorsForward = 13
PinLeftMotorsBackward = 15

runtime = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PinRightMotorsForward, GPIO.OUT)
GPIO.setup(PinRightMotorsBackward, GPIO.OUT)

GPIO.setup(PinLeftMotorsForward, GPIO.OUT)
GPIO.setup(PinLeftMotorsBackward, GPIO.OUT)


def run_forward():
    GPIO.output(PinRightMotorsForward, GPIO.HIGH)
    GPIO.output(PinLeftMotorsForward, GPIO.HIGH)
    print("running forward")
    time.sleep(runtime)
    stop()


def turn_right():
    GPIO.output(PinLeftMotorsForward, GPIO.HIGH)
    GPIO.output(PinRightMotorsBackward, GPIO.HIGH)
    print("turning right")
    time.sleep(runtime)
    stop()


def turn_left():
    GPIO.output(PinRightMotorsForward, GPIO.HIGH)
    GPIO.output(PinLeftMotorsBackward, GPIO.HIGH)
    print("turning right")
    time.sleep(runtime)
    stop()


def run_reverse():
    GPIO.output(PinRightMotorsBackward, GPIO.HIGH)
    GPIO.output(PinLeftMotorsBackward, GPIO.HIGH)
    print("running backward")
    time.sleep(runtime)
    stop()


def stop_running():
    GPIO.output(PinRightMotorsForward, GPIO.LOW)
    GPIO.output(PinRightMotorsBackward, GPIO.LOW)
    GPIO.output(PinLeftMotorsForward, GPIO.LOW)
    GPIO.output(PinLeftMotorsBackward, GPIO.LOW)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
