from constants import *
import json,os
import numpy as np
from tqdm import tqdm

def get_mapillary_token():
    with open('mapillary_token', 'r') as f:
        return f.readline()

def dump_json(data, filename,encoding='utf-8'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)

def read_json(filename,encoding='utf-8'):
    with open(filename, 'r') as f:
        return json.load(f)

# def get_mly_img_data(img_id):
#     return json.loads(mly.image_from_key(img_id))

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

# function to return a random entry in a list:
def random_entry(input_list):
    return input_list[np.random.randint(len(input_list))]

def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# function to iterate through all folders in a directory, returning full paths to all subfolders contained within
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def find_matching_folderpath(basefolderpath,foldername):
    folderpath_list = listdir_fullpath(basefolderpath)

    for folderpath in folderpath_list:
        if foldername in folderpath:
            return folderpath
    
# a function that searches recursively into all subfolders of a folder and returns the first folder that contains the foldername
def find_folder_recursive(path, foldername):
    for root, dirs, files in os.walk(path):
        if foldername in dirs:
            return os.path.join(root, foldername)
        
def parse_pointcloud(filepath,outpath=None):
    import struct

    size_float = 4
    list_pcd = []
    with open(filepath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z, intensity])
            byte = f.read(size_float * 4)
    
    if outpath:
        np.savetxt(outpath,np.asarray(list_pcd))

    return np.asarray(list_pcd)

def save_as_pointcloud(depth_data,img,f, outpath,invertRB=False):
    H, W, _ = img.shape

    ref_dim = max(H,W)

    f = f * ref_dim

    t_h = (H - 1)/2 
    t_w = (W - 1)/2 

    with open(outpath,'w+') as writer:
        for c in tqdm(range(W)):
            for l in range(H):
                pi = np.array([c-t_w,l-t_h,f])
                pn = pi / np.linalg.norm(pi)

                p = pn * depth_data[l,c]

                color = img[l,c]

                if color[0] == 255 and color[1] == 255 and color[2] == 255:
                    pass
                else:
                    writer.write(f'{p[0]:.3f},{p[1]:.3f},{p[2]:.3f},{color[2]},{color[1]},{color[0]}\n')

def prepare_img_data_dict(json_path):
    img_metadata = read_json(json_path)

    new_dict = {}

    for entry in img_metadata['data']:
        new_dict[entry['id']] = entry

    return new_dict

# function to get filename from a path:
def get_filename_from_path(path, with_extension=False):
    filename = os.path.basename(path)
    if with_extension:
        return filename
    return filename.split('.')[0]
