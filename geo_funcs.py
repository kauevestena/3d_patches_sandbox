import geopandas as gpd
import numpy as np
import os

# a function that returns the geometry of a random rown in a geodataframe:
def random_geometry(inputpath):
    input_gdf = gpd.read_file(inputpath)
    random_row = input_gdf.iloc[np.random.randint(len(input_gdf))]
    if random_row.geometry.geom_type == 'Point':
        return tuple(random_row.geometry.coords[0])
    else:
        return random_geometry(inputpath)
    
def random_geometry_with_capture(inputpath,cap_key='capture'):
    input_gdf = gpd.read_file(inputpath)

    filename = os.path.basename(inputpath).split('.')[0]

    random_row = input_gdf.iloc[np.random.randint(len(input_gdf))]
    if random_row.geometry.geom_type == 'Point':
        return tuple(random_row.geometry.coords[0]), random_row[cap_key], filename
    else:
        return random_geometry(inputpath)
    
