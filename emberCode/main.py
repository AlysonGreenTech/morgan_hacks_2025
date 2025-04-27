import socket  # Import the standard library socket module
from flask_socketio import SocketIO
from flask import Flask, render_template
import time
import envSensor as env 
import imu
import gps
import rangeFinder
import os
import asyncio
import motorControl as mc


temp = 0
barometer = 0
accel_x = 0
accel_y = 0
accel_z = 0
gps_lat = 0
gps_lon = 0
motion_detection = 0


# Flask Set up
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Rename this variable to avoid conflict
print("Flask SocketIO initialized")
server_ip = "127.0.0.1"  # Use the standard library socket module

# Main page
@app.route("/")
def main():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    print("server started")
    # Dynamically get the host IP address
    server_ip = socket.gethostbyname(socket.gethostname())  # Use the standard library socket module
    # print("Server IP Address: " + server_ip)
    return render_template("EMBER.html", api_key=api_key, server_ip=server_ip)

# WebSocket Events
@socketio.on('connect')
def handleConnect():
    print("WebSocket connected")

@socketio.on('disconnect')
def handleDisconnect():
    print("WebSocket disconnected")

@socketio.on('message')
def handleMsg(msg):
    # Step 1: Send Sensor Data over WebSocket
    # print(msg)
    if msg == "Controller Connected":
        socketio.send([voltage, 
                   internal_temp, internal_humidity,
                   external_temp, external_humidity,
                   pyr_x, pyr_y, pyr_z, 
                   accel_x, accel_y, accel_z, 
                   mag_x, mag_y, mag_z,
                   gps_lat, gps_lon,
                   range_finder])
    else:
        mc.drive(msg[0],msg[1])
        mc.actuation(msg[2],msg[3],msg[4],msg[5])
        socketio.send([voltage, 
                   internal_temp, internal_humidity,
                   external_temp, external_humidity,
                   pyr_x, pyr_y, pyr_z, 
                   accel_x, accel_y, accel_z, 
                   mag_x, mag_y, mag_z,
                   gps_lat, gps_lon,
                   range_finder])
    # print("Message Received: " + msg)

# Async updates
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
        pyr_x, pyr_y, pyr_z, accel_x, accel_y, accel_z, mag_x, mag_y, mag_z = imu.getIMU()
        await asyncio.sleep(0.4)

async def update_gps():
    global gps_lat, gps_lon
    while True:
        new_lat, new_lon = gps.getGPS()
        if new_lat is not None and new_lon is not None:
            gps_lat, gps_lon = new_lat, new_lon
        await asyncio.sleep(60)

async def update_rangefinder():
    global range_finder
    while True:
        range_finder = rangeFinder.getLidarData()
        await asyncio.sleep(5)

# Run both coroutines concurrently
async def updateAllSensors():
    await asyncio.gather(
        update_voltage(),
        update_internal_temp(),
        update_internal_humidity(),
        update_external_temp(),
        update_external_humidity(),
        update_imu(),
        update_gps(),
        update_rangefinder()
    )

# Start Flask Server w/ SocketIO
if __name__ == "__main__":
    # Start the async tasks in a separate thread
    def start_async_tasks():
        asyncio.run(updateAllSensors())

    from threading import Thread
    Thread(target=start_async_tasks, daemon=True).start()

    # Run the Flask-SocketIO server
    socketio.run(app, host=server_ip, port=5000)