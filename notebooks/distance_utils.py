import numpy as np

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two locations.

    Parameters:
        lat1: Pickup latitude
        lon1: Pickup longitude
        lat2: Dropoff latitude
        lon2: Dropoff longitude

    Returns:
        Distance in kilometers
    """

    # Difference in latitude and longitude
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Convert degrees to radians
    r_lat1 = np.radians(lat1)
    r_lat2 = np.radians(lat2)
    r_delta_lat = np.radians(delta_lat)
    r_delta_lon = np.radians(delta_lon)

    # Haversine formula
    part1 = np.sin(r_delta_lat / 2) ** 2

    part2 = (
        np.cos(r_lat1)
        * np.cos(r_lat2)
        * np.sin(r_delta_lon / 2) ** 2
    )

    a = part1 + part2

    # Calculate angular distance
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Earth's radius in kilometers
    R = 6371

    # Distance
    distance = R * c

    return distance
