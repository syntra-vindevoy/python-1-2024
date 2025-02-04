import math
from mgrs import MGRS

def calculate_fire_elements(firing_position_mgrs, target_position_mgrs, firing_altitude, target_altitude, lateral_deviation, firing_table, deflection_table):
    """
    Calculate direction, deflection, elevation, and charge for an 81mm mortar using HE firing tables and deflection correction table.

    Parameters:
        firing_position_mgrs (str): Firing position in MGRS coordinates.
        target_position_mgrs (str): Target position in MGRS coordinates.
        firing_altitude (float): Altitude of the firing position in meters.
        target_altitude (float): Altitude of the target in meters.
        lateral_deviation (float): Lateral deviation in meters.
        firing_table (list): Firing table with charge, range, and elevation.
        deflection_table (dict): Deflection table as a dictionary of ranges and deflection values.

    Returns:
        dict: Contains direction (mils), deflection (mils), elevation (mils), and charge.
    """
    mgrs_converter = MGRS()

    # Convert MGRS to UTM coordinates
    firing_position = mgrs_converter.toLatLon(firing_position_mgrs)
    target_position = mgrs_converter.toLatLon(target_position_mgrs)

    # Convert lat/lon to meters (assuming flat earth for simplicity)
    x1, y1 = firing_position
    x2, y2 = target_position

    # Step 1: Calculate direction (mils)
    dx = x2 - x1
    dy = y2 - y1
    azimuth_deg = math.degrees(math.atan2(dy, dx))
    direction_mils = int(azimuth_deg * (3200 / 360))

    # Step 2: Calculate range (meters)
    range_m = math.sqrt(dx**2 + dy**2)

    # Step 3: Adjust for altitude difference
    dz = target_altitude - firing_altitude

    # Step 4: Find charge and elevation from firing table
    for charge_data in firing_table:
        charge = charge_data["charge"]
        min_range = charge_data["min_range"]
        max_range = charge_data["max_range"]
        elevation_base = charge_data["elevation_base"]

        if min_range <= range_m <= max_range:
            # Adjust elevation for altitude difference
            elevation_adjusted = elevation_base + int(dz / 10)  # Simplified adjustment

            # Step 5: Calculate deflection (mils) from deflection table
            if int(range_m) in deflection_table:
                deflection_meters = deflection_table[int(range_m)]
                deflection_mils = int((lateral_deviation / range_m) * 1000)
            else:
                deflection_mils = 0  # Default to 0 if range is out of table bounds

            return {
                "direction_mils": direction_mils,
                "deflection_mils": deflection_mils,
                "elevation_mils": elevation_adjusted,
                "charge": charge
            }

    return {"error": "Target out of range for available charges."}

# Example Firing Table
firing_table = [
    {"charge": 1, "min_range": 200, "max_range": 800, "elevation_base": 1200},
    {"charge": 2, "min_range": 800, "max_range": 1500, "elevation_base": 1150},
    {"charge": 3, "min_range": 1500, "max_range": 3000, "elevation_base": 1100},
    {"charge": 4, "min_range": 3000, "max_range": 4800, "elevation_base": 1050},
    {"charge": 5, "min_range": 4800, "max_range": 5600, "elevation_base": 1000},
    {"charge": 6, "min_range": 5600, "max_range": 6400, "elevation_base": 950},
]

# Example Deflection Table (Simplified for ranges 500-4000m)
deflection_table = {
    500: 20, 600: 17, 700: 15, 800: 13, 900: 11, 1000: 10,
    1500: 7, 2000: 5, 2500: 4, 3000: 3, 3500: 3, 4000: 2
}

# Example Usage
firing_position_mgrs = "33TWN0000000000"  # Replace with actual MGRS
target_position_mgrs = "33TWN0010001000"  # Replace with actual MGRS
firing_altitude = 100           # Altitude of firing position (m)
target_altitude = 50            # Altitude of target position (m)
lateral_deviation = 20          # Lateral deviation in meters

result = calculate_fire_elements(
    firing_position_mgrs, target_position_mgrs, firing_altitude,
    target_altitude, lateral_deviation, firing_table, deflection_table
)

print(result)
