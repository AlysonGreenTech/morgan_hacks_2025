import socket  # Import the standard library socket module
from flask_socketio import SocketIO
from flask import Flask, render_template
import time
import envSensor as env 
import imu
import gps
import os
import asyncio
import motorControl as mc

# Global Variables
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
        socketio.send([temp, barometer,
                   accel_x, accel_y, accel_z,
                   gps_lat, gps_lon,
                   motion_detection])
    else:
        mc.drive(msg[0],msg[1])
        mc.actuation(msg[2],msg[3],msg[4],msg[5])
        effect.led(msg[6])
        effect.buzzer(msg[7])
        socketio.send([temp, barometer,
                   accel_x, accel_y, accel_z,
                   gps_lat, gps_lon,
                   motion_detection])
    # print("Message Received: " + msg)

# Async updates
async def update_barometer():
    global barometer
    while True:
        barometer = env.getBaro()
        await asyncio.sleep(0.4)

async def update_temp():
    global temp
    while True:
        temp = env.getTemp()
        await asyncio.sleep(0.4)

async def update_imu():
    global accel_x, accel_y, accel_z
    while True:
        accel_x, accel_y, accel_z = imu.getIMU()
        await asyncio.sleep(0.4)

async def update_gps():
    global gps_lat, gps_lon
    while True:
        new_lat, new_lon = gps.getGPS()
        if new_lat is not None and new_lon is not None:
            gps_lat, gps_lon = new_lat, new_lon
        await asyncio.sleep(60)

async def update_motion():
    global motion_detection
    while True:
        motion_detection = imu.getMotion()
        await asyncio.sleep(0.4)



# Run both coroutines concurrently
async def updateAllSensors():
    await asyncio.gather(
        update_barometer(),
        update_temp(),
        update_motion(),
        update_imu(),
        update_gps()
    )

# Start Flask Server w/ SocketIO
if __name__ == "__main__":
    # Start the async tasks in a separate thread
    def start_async_tasks():
        asyncio.run(updateAllSensors())

    from threading import Thread
    Thread(target=start_async_tasks, daemon=True).start()

    # Run the Flask-SocketIO server
    socketio.run(app, host=server_ip, port=4040)