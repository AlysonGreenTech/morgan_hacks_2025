import socket

hostname = socket.gethostname()  # Get the local machine name
local_ip = socket.gethostbyname(hostname)  # Get the local IP address
print("Hostname: ", hostname)
print("Local IP Address: ", local_ip)