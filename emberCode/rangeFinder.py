import random
import time
import smbus

# def getRangeFinder(): #TODO: Implement actual sensor reading
#     # Get the range finder value
#     random.seed(time.time())
#     return (random.randint(0, 8))

def getLidarData():
    bus = smbus.SMBus(1) # Change the I2C bus number based on the actual device
    addr = 0x10 # Radar default address 0x10
    cmd = [0x5A,0x05,0x00,0x01,0x60] # Gets the distance value instruction
    bus.write_i2c_block_data(addr, 0x00, cmd)
    time.sleep(0.01)
    data = bus.read_i2c_block_data(addr, 0x00, 9)

    distance = data[0] | (data[1] << 8)
    distance =distance /  100
    return distance


# getLidarData()
# time.sleep(0.1)