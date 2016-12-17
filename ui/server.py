from flask import Flask
from flask import render_template
import GPIOEmu as GPIO
# import RPi.GPIO as GPIO

app = Flask(__name__)


class Car:

    def __init__(self):
        self.__PinRightMotorsForward__ = 38
        self.__PinRightMotorsBackward__ = 40
        self.__PinLeftMotorsForward__ = 13
        self.__PinLeftMotorsBackward__ = 15
        self.__initializeGPIO__()

    def __initializeGPIO__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__PinRightMotorsForward__, GPIO.OUT)
        GPIO.setup(self.__PinRightMotorsBackward__, GPIO.OUT)
        GPIO.setup(self.__PinLeftMotorsForward__, GPIO.OUT)
        GPIO.setup(self.__PinLeftMotorsBackward__, GPIO.OUT)
        self.__reset_inputs__()

    def run_forward(self):
        self.__reset_inputs__()
        GPIO.output(self.__PinRightMotorsForward__, GPIO.HIGH)
        GPIO.output(self.__PinLeftMotorsForward__, GPIO.HIGH)
        print("running forward")

    def turn_right(self):
        self.__reset_inputs__()
        GPIO.output(self.__PinLeftMotorsForward__, GPIO.HIGH)
        GPIO.output(self.__PinRightMotorsBackward__, GPIO.HIGH)
        print("turning right")

    def turn_left(self):
        self.__reset_inputs__()
        GPIO.output(self.__PinRightMotorsForward__, GPIO.HIGH)
        GPIO.output(self.__PinLeftMotorsBackward__, GPIO.HIGH)
        print("turning right")

    def run_reverse(self):
        self.__reset_inputs__()
        GPIO.output(self.__PinRightMotorsBackward__, GPIO.HIGH)
        GPIO.output(self.__PinLeftMotorsBackward__, GPIO.HIGH)
        print("running backward")

    def stop(self):
        self.__reset_inputs__()

    def __reset_inputs__(self):
        GPIO.output(self.__PinRightMotorsForward__, GPIO.LOW)
        GPIO.output(self.__PinRightMotorsBackward__, GPIO.LOW)
        GPIO.output(self.__PinLeftMotorsForward__, GPIO.LOW)
        GPIO.output(self.__PinLeftMotorsBackward__, GPIO.LOW)

car = Car()


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/move/forward")
def forward():
    car.run_forward()
    return "OK"


@app.route("/move/left")
def left():
    car.turn_left()
    return "OK"


@app.route("/move/right")
def right():
    car.turn_right()
    return "OK"


@app.route("/move/backward")
def backward():
    car.run_reverse()
    return "OK"


@app.route("/stop")
def stop():
    car.stop()
    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
