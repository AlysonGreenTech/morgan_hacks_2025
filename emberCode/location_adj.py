import math

def calculate_new_coordinates(lat, lon, distance, angle):
    """
    Calculate new coordinates after moving a certain distance at a specific angle
    using the Haversine formula.

    Parameters:
    - lat: Latitude of the starting point in degrees
    - lon: Longitude of the starting point in degrees
    - distance: Distance to move in meters
    - angle: Angle of movement in degrees (0 = north, 90 = east)

    Returns:
    - (new_lat, new_lon): Tuple of new latitude and longitude in degrees
    """
    # Convert latitude, longitude, and angle to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    angle_rad = math.radians(angle)

    # Earth's radius in meters
    R = 6378137

    # Calculate the new latitude in radians
    new_lat_rad = lat_rad + (distance / R) * math.cos(angle_rad)

    # Calculate the new longitude in radians
    new_lon_rad = lon_rad + (distance / R) * math.sin(angle_rad) / math.cos(lat_rad)

    # Convert the new latitude and longitude back to degrees
    new_lat = math.degrees(new_lat_rad)
    new_lon = math.degrees(new_lon_rad)

    return new_lat, new_lon

# Example usage
start_lat = 39.35092080657169
start_lon = -76.58070020630689
distance = 20  # in meters
angle = 30  # in degrees

new_lat, new_lon = calculate_new_coordinates(start_lat, start_lon, distance, angle)
print(f"New coordinates: Latitude = {new_lat}, Longitude = {new_lon}")