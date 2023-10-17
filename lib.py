from constants import *
import json,os
import mapillary.interface as mly
import numpy as np


def get_mapillary_token():
    with open('mapillary_token', 'r') as f:
        return f.readline()

def dump_json(data, filename,encoding='utf-8'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)

def read_json(filename,encoding='utf-8'):
    with open(filename, 'r') as f:
        return json.load(f)

def get_mly_img_data(img_id):
    return json.loads(mly.image_from_key(img_id))

def calculate_angle_between_vectors(vector1, vector2,return_radians=False):
    # Calculate the dot product of the two vectors
    dot_product = np.dot(vector1, vector2)
    
    # Calculate the magnitudes of the two vectors
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    # Calculate the cosine of the angle between the vectors
    cosine_theta = dot_product / (magnitude1 * magnitude2)
    
    # Calculate the angle in radians
    angle_radians = np.arccos(cosine_theta)
    
    if return_radians:
        return angle_radians

    else:
    # Convert the angle from radians to degrees
        angle_degrees = np.degrees(angle_radians)
        return angle_degrees

