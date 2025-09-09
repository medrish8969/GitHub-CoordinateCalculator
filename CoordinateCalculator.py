#/ usr/bin/evn python
# -*- coding: utf-8 -*-

"""
  Name:  CoordinateCalculator.py
  Description:  Converts geographic coordinates in DDMMSS format to DD
  Created:  September 9, 2025
  Author:  Maria Binte Edrish (medrish@ksu.edu)
  Python Version:  3.11.11
"""
# Ask user for input
coord_str = input("Enter your coordinate in DDMMSS format:461107")

# Extract parts: first 2 = degrees, next 2 = minutes, last 2 = seconds
degrees = int(coord_str[0:2])
minutes = int(coord_str[2:4])
seconds = int(coord_str[4:6])
print("Degrees:", degrees, "Minutes:", minutes, "Seconds:", seconds)

# Convert to decimal degrees
decimal_degrees = degrees + minutes/60 + seconds/3600

# Round to two decimal places
decimal_degrees = round(decimal_degrees, 2)

print("Your final result is:", decimal_degrees, "degrees")