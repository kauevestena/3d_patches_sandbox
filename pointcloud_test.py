import numpy as np
import mapillary as mly
import json
from lib import *
import cv2
from tqdm import tqdm

img_data = read_json('image_data.json')

img = cv2.imread('inputs/sample_mapillary.jpeg')

depth_data = np.load('inputs/depthmap2.npy')

H,W,d = img.shape

t_h = (H - 1)/2 
t_w = (W - 1)/2 

print(depth_data.shape,H,W)

ref_dim = max(H,W)

f = img_data['features']['properties']['camera_parameters'][0] * ref_dim

f_alternate = 0.788 * ref_dim


with open('point_cloud_v2.xyz','w+') as writer:
    for c in tqdm(range(W)):
        for l in range(H):
            pi = np.array([c-t_w,l-t_h,f_alternate])
            pn = pi / np.linalg.norm(pi)

            p = pn * depth_data[l,c]

            color = img[l,c]

            writer.write(f'{p[0]:.3f},{p[1]:.3f},{p[2]:.3f},{color[2]},{color[1]},{color[0]}\n')




