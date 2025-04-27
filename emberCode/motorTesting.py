import time
import RPi.GPIO as GPIO
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit 
from board import SCL, SDA
import busio
# Create the I2C bus interface
i2c_bus = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance
pca = PCA9685(i2c_bus)

def actuation(pitchDeg, yawDeg, baseDeg):
    move = ServoKit(channels = 16)
    base = 0
    baseRef = 1
    yaw = 2
    pitch = 3

    move.servo[base].angle = int(baseDeg)
    move.servo[baseRef].angle = (-1*baseDeg) +180
    move.servo[yaw].angle = yawDeg    
    move.servo[pitch].angle = pitchDeg

while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enter 'a' for actuation, 's' for stop, 'f' for forward, 'b' for backward, 'l' for left turn, 'r' for right turn")
        
        ch = input("ch: ")  # Input is a string, don't convert it to int immedi>
        if ch == "s":
                for channel in range(16):
                        

                        GPIO.setmode(GPIO.BCM)
                        pins = [19, 16, 26, 20]
                        for pin in pins:
                                GPIO.setup(pin, GPIO.OUT)
                                GPIO.output(pin, GPIO.LOW)
                print("STOP")
        elif ch == "a":
                pitchDeg = int(input("Pitch Degrees: "))
                yawDeg = int(input("Yaw Degrees: "))
                baseDeg = int(input("Base Degrees: "))
                actuation(pitchDeg, yawDeg, baseDeg)
        elif ch == "f":
                
                print("FORWARD")
        elif ch == "b":
                
                print("BACKWARD")
        elif ch == "l":
                
                print("LEFT TURN")
        elif ch == "r":
                
                print("RIGHT TURN")
        else:
                print("Invalid input, please try again.")
                continue
        time.sleep(0.5)  # Add a small delay to avoid overwhelming the input