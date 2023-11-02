import requests
import os
import json
import numpy as np
from shapely.geometry import Point, box
from math import cos, pi
import urllib

# download the following number of random mappilary images
n_downloads = 1000

# the search must be done in this bounding box:
bbox = (8.306007,48.955650,8.502388,49.061270) 

# get the token
with open('mapillary_token', 'r') as f:
    token = f.readline()

#function to define a random lat, lon in the bounding box:
def random_point_in_bbox(input_bbox):
    """
    Generate a random point within a given bounding box.

    Parameters:
        bbox (list): A list containing the coordinates of the bounding box in the format [min_lon, min_lat, max_lon, max_lat].

    Returns:
        tuple: A tuple containing the latitude and longitude of the randomly generated point.
    """
    min_lon, min_lat, max_lon, max_lat = input_bbox
    lat = min_lat + (max_lat - min_lat) * np.random.random()
    lon = min_lon + (max_lon - min_lon) * np.random.random()
    return lon, lat




# generate a sample to test the function, using a csv file:
with open('sample_random_coords.csv', 'w+') as f:
    f.write('lon, lat\n')
    for i in range(100):
        lon, lat = random_point_in_bbox(bbox)
        f.write(f'{lon}, {lat}\n')

import requests

def get_mapillary_images(minLat, minLon, maxLat, maxLon, token):
    """
    Request images from Mapillary API given two coordinates and radius.

    Parameters:
        minLat (float): The latitude of the first coordinate.
        minLon (float): The longitude of the first coordinate.
        maxLat (float): The latitude of the second coordinate.
        maxLon (float): The longitude of the second coordinate.
        token (str): The Mapillary API token.

    Returns:
        dict: A dictionary containing the response from the API.
    """
    url = "https://graph.mapillary.com/images"
    params = {
        "bbox": f"{minLon},{minLat},{maxLon},{maxLat}",
        "access_token": token,
        "fields": ",".join([
            "altitude", 
            "atomic_scale", 
            "camera_parameters", 
            "camera_type", 
            "captured_at",
            "compass_angle", 
            "computed_altitude", 
            "computed_compass_angle", 
            "computed_geometry",
            "computed_rotation", 
            "creator", 
            "exif_orientation", 
            "geometry", 
            "height", 
            # "is_pano",
            "make", 
            "model", 
            # "thumb_256_url", 
            # "thumb_1024_url", 
            # "thumb_2048_url",
            "thumb_original_url", 
            "merge_cc", 
            # "mesh", 
            "sequence", 
            # "sfm_cluster", 
            "width",
            # "detections",
        ])
    }
    response = requests.get(url, params=params)
    return response.json()

def radius_to_degrees(radius,lat):
    """
    Convert a radius in meters to degrees.  
    """
    return radius / (111320 * cos(lat * pi / 180))

def get_bounding_box(lon, lat, radius):
    """
    Return a bounding box tuple as (minLon, minLat, maxLon, maxLat) from a pair of coordinates and a radius, using shapely.

    Parameters:
        lon (float): The longitude of the center of the bounding box.
        lat (float): The latitude of the center of the bounding box.
        radius (float): The radius of the bounding box in meters.

    Returns: 
        tuple: A tuple containing the minimum and maximum longitude and latitude of the bounding box.
    """


    # Convert radius from meters to degrees
    radius_deg = radius_to_degrees(radius, lat)

    point = Point(lon, lat)
    return box(point.x - radius_deg, point.y - radius_deg, point.x + radius_deg, point.y + radius_deg).bounds

# wraping it all up: generating a random point, compute a 20m bounding box and request the images:
point = (8.4036232,49.0052406)

point_bbox = get_bounding_box(point[0], point[1], 20)

response = get_mapillary_images(point_bbox[1], point_bbox[0], point_bbox[3], point_bbox[2], token)

# read the response as a GeoDataFrame:
# import geopandas as gpd

# gdf = gpd.GeoDataFrame.from_features(response['data'])

# gdf.to_file('sample_image_data.geojson', driver='GeoJSON')

#saving the response:
with open('sample_image_data.json', 'w+',encoding='utf-8') as f:
    json.dump(response, f, indent=4,ensure_ascii=False)

# for image in response['data']:
#     print(image['thumb_256_url'])