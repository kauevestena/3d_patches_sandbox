from mappilary_funcs import *

# KITTI_rootpath = '..\KITTI_lidar\data'



# first_part = find_matching_folderpath(KITTI_rootpath,'2011_09_26_drive_0106_sync')

# print(find_folder_recursive(first_part,'velodyne_points'))

img_data = get_mapillary_images(*get_bounding_box(*(48.99820,8.46871), 30), get_mapillary_token(),'test.json')

for i,entry in enumerate(img_data['data']):
    if url := entry.get('thumb_original_url'):
        download_mapillary_image(url,f'tests\\tests{i}.jpg')