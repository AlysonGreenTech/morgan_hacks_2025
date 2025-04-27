import random
import time
from icm20948 import ICM20948

def getIMU(): #TODO: Implement actual sensor reading
    # random.seed(time.time())
    # return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    try:
        sensor = ICM20948(i2c_addr=0x69)
        ax, ay, az= sensor.read_accelerometer_gyro_data()
        return (ax, ay, az)
    except OSError as e:
        print(f"Error accessing the sensor: {e}")
        return None