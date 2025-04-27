import envSensor as env 
import imu
import gps
import rangeFinder


for idx in range(10):
    print([env.getVoltage(), 
           env.getTemp(), 
           env.getHumidity(),
           imu.getPYR()[0], imu.getPYR()[1], imu.getPYR()[2], 
           imu.getAccelXYZ()[0], imu.getAccelXYZ()[1], imu.getAccelXYZ()[2], 
           imu.getMagXYZ()[0], imu.getMagXYZ()[1], imu.getMagXYZ()[2],
           gps.getGPS()[0], gps.getGPS()[1],
           rangeFinder.getRangeFinder()])