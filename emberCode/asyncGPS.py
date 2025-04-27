import random
import asyncio

theValue = 0

voltage = 0
internal_temp = 0
internal_humidity = 0
external_temp = 0
external_humidity = 0
pyr_x = 0
pyr_y = 0
pyr_z = 0
accel_x = 0
accel_y = 0
accel_z = 0
mag_x = 0
mag_y = 0
mag_z = 0
gps_lat = 0
gps_lon = 0
range_finder = 0

async def update_voltage():
    global voltage
    while True:
        voltage = env.getVoltage()
        await asyncio.sleep(0.1)

async def update_internal_temp():
    global internal_temp
    while True:
        internal_temp = env.getInternalTemp()
        await asyncio.sleep(0.1)

async def update_internal_humidity():
    global internal_humidity
    while True:
        internal_humidity = env.getInternalHumidity()
        await asyncio.sleep(0.1)

async def update_external_temp():
    global external_temp
    while True:
        external_temp = env.getExternalTemp()
        await asyncio.sleep(0.1)

async def update_external_humidity():
    global external_humidity
    while True:
        external_humidity = env.getExternalHumidity()
        await asyncio.sleep(0.1)

async def update_imu():
    global pyr_x, pyr_y, pyr_z, accel_x, accel_y, accel_z, mag_x, mag_y, mag_z
    while True:
        pyr_x, pyr_y, pyr_z = imu.getPYR()
        accel_x, accel_y, accel_z = imu.getAccelXYZ()
        mag_x, mag_y, mag_z = imu.getMagXYZ()
        await asyncio.sleep(0.1)

async def update_gps():
    global gps_lat, gps_lon
    while True:
        gps_lat, gps_lon = gps.getGPS()
        await asyncio.sleep(2)



# Run both coroutines concurrently
async def main():
    await asyncio.gather(
        update_voltage(),
        update_internal_temp(),
        update_internal_humidity(),
        update_external_temp(),
        update_external_humidity(),
        update_imu(),
        update_gps()
    )

asyncio.run(main())