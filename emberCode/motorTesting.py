import time
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit 
from board import SCL, SDA
import busio
# Create the I2C bus interface
i2c_bus = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance
pca = PCA9685(i2c_bus)

def set_pwm(channel, frequency, duty_cycle):
    # Set the PWM frequency
    pca.frequency = frequency
    # Calculate the pulse length
    pulse_length = int(duty_cycle * 65535 / 100)
    # Set the PWM signal for the specified channel
    pca.channels[channel].duty_cycle = pulse_length

def actuation(pitchDeg, yawDeg, armHeight, baseDeg):
    move = ServoKit(channels = 16)
    base = 0
    baseRef = 1
    yaw = 2
    pitch = 3
    linact = 4

    move.servo[base].angle = int(baseDeg)
    move.servo[baseRef].angle = (-1*baseDeg) +180
    move.servo[yaw].angle = yawDeg    
    move.servo[pitch].angle = pitchDeg
    move.servo[linact].angle = armHeight

while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Enter 'a' for actuation, 's' for stop, 'f' for forward, 'b' for backward, 'l' for left turn, 'r' for right turn")
        
        ch = input("ch: ")  # Input is a string, don't convert it to int immedi>
        if ch == "s":
                for channel in range(16):
                        set_pwm(channel, 50, 0)
                print("STOP")
        elif ch == "a":
                pitchDeg = int(input("Pitch Degrees: "))
                yawDeg = int(input("Yaw Degrees: "))
                armHeight = int(input("Arm Height: "))
                baseDeg = int(input("Base Degrees: "))
                actuation(pitchDeg, yawDeg, armHeight, baseDeg)
        elif ch == "f":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(13, frequency, duty_cycle)
                set_pwm(14, frequency, duty_cycle)
                print("FORWARD")
        elif ch == "b":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(15, frequency, duty_cycle)
                set_pwm(12, frequency, duty_cycle)
                print("BACKWARD")
        elif ch == "l":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(14, frequency, duty_cycle)
                set_pwm(12, frequency, duty_cycle)
                print("LEFT TURN")
        elif ch == "r":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(13, frequency, duty_cycle)
                set_pwm(15, frequency, duty_cycle)
                print("RIGHT TURN")
        else:
                try:
                        ch = int(ch)
                        frequency = int(input("Freq: "))
                        duty_cycle = int(input("DC%: "))
                        set_pwm(ch, frequency, duty_cycle)
                except ValueError:
                        print("Invalid input. Please try again.")