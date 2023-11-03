import requests
import os
import json
import numpy as np
from shapely.geometry import Point, box
from math import cos, pi
import urllib
from mapillary_funcs import *

# download the following number of random mappilary images
n_downloads = 1000

# the search must be done in this bounding box:
bbox = (8.306007,48.955650,8.502388,49.061270) 

# get the token
with open('mapillary_token', 'r') as f:
    token = f.readline()

# generate a sample to test the function, using a csv file:
with open('sample_random_coords.csv', 'w+') as f:
    f.write('lon, lat\n')
    for i in range(100):
        lon, lat = random_point_in_bbox(bbox)
        f.write(f'{lon}, {lat}\n')

import requests



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