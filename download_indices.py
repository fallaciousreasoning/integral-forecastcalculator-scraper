
import os
from client import ApiClient

file_name = 'output/site_indices.csv'
has_points = set()

def has_point(point):
    """Check if we've already downloaded a point. If we have, skip it."""
    lat, lng = point
    return (lat, lng) in has_points

def load_points():
    """Add all points we've already downloaded to the file, so we don't download them multiple times"""
    if not os.path.exists(file_name):
        return

    with open(file_name) as f:
        lines = f.readlines()[1:] # Skip the header row
        for line in lines:
            parts = line.split(',')
            lat = float(parts[0])
            lng = float(parts[1])

            has_points.add((lat, lng))

def maybe_write_header():
    if os.path.exists(file_name):
        return
    with open(file_name, 'w') as f:
        f.write(f'lat, lng, altitude, siteIndex, the300index, the500index\n')

def write_line(lat, lng, altitude, siteIndex, index300, index500):
    with open(file_name, 'a') as f:
        f.write(f'{lat}, {lng}, {altitude}, {siteIndex}, {index300}, {index500}\n')

def parse_input_points(input_file):
    with open(input_file) as f:
        lines = f.readlines()[1:] # Skip the header row
        for line in lines:
            parts = line.split(',')
            lat = float(parts[0])
            lng = float(parts[1])
            yield (lat, lng)


if __name__ == "__main__":
    # Load the points which we've already downloaded. This is useful if we crash halfway through.
    load_points()
    # Write the header line, if the file doesn't already exist.
    maybe_write_header()

    # Your login details here...
    client = ApiClient('jay.harris@outlook.co.nz', 'xsEn2xxwCLsty3')

    # Note: This file needs to be a CSV of Latitude, Longitude (not Longitude, Latitude)
    input_points = list(parse_input_points('input/input_points.csv'))

    done = 0
    for point in input_points:
        done += 1

        # If we've already got the info about this point, skip it.
        if has_point(point):
            continue

        indices = client.get_indices(point[0], point[1])
        write_line(indices['latitude'], indices['longitude'], indices['altitude'], indices['siteIndex'], indices['the300Index'], indices['the500Index'])
        
        print(f'Progress: {done+1}/{len(input_points)}') # Let the user know how we're doing.

    print(f"Done! Indices are in the file {file_name}")
