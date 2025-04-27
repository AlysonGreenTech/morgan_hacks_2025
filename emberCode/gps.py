import subprocess
import pynmea2

def getGPS():  # returns lat, lon
    try:
        # Run the command with sudo privileges
        process = subprocess.Popen(
            ["sudo", "cat", "/dev/ttyAMA0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Capture output as a string
        )

        # Continuously read the output line by line
        for line in process.stdout:
            if line.startswith("$GPGGA"):  # Check if the line starts with $GPGGA
                msg = pynmea2.parse(line.strip())  # Parse the NMEA sentence
                print(float(msg.latitude), float(msg.longitude))
                return float(msg.latitude), float(msg.longitude)  # Return latitude and longitude

        # If no valid GPS data is found, return a default value
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None  # Return None for both latitude and longitude in case of an error

