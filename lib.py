from constants import *
import json,os
import mapillary.interface as mly


def get_mapillary_token():
    with open('mapillary_token', 'r') as f:
        return f.readline()

def dump_json(data, filename,encoding='utf-8'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)

def get_mly_img_data(img_id):
    return json.loads(mly.image_from_key(img_id))