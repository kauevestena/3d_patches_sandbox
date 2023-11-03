from mappilary_funcs import *
import shutil

layers_path = r'..\kitti_loc_scripts\layers'

outfolder_basepath = r'..\sample_mapillary_data'

filelist = listdir_fullpath(layers_path)

mappilary_token = get_mapillary_token()

KITTI_rootpath = '..\KITTI_lidar\data'


radius = 30


for i in range(1000):
    random_filepath = random_entry(filelist)

    point, capture, sequence = random_geometry_with_capture(random_filepath)

    print(point,capture,sequence)

    outname = f'{sequence}_{capture}'

    outfolderpath = os.path.join(outfolder_basepath, outname)

    create_folder_if_not_exists(outfolderpath)

    out_jsonpath = os.path.join(outfolderpath, outname + '.json')

    # getting imagery metadata from mappilary:
    img_data = get_mapillary_images(*get_bounding_box(point[1],point[0], radius), mappilary_token, out_jsonpath)

    if img_data.get('data'):
        imgs_outpath = os.path.join(outfolderpath,'images')

        create_folder_if_not_exists(imgs_outpath)

        for entry in img_data['data']:
            if url := entry.get('thumb_original_url'):
                img_id = entry['id']
                download_mapillary_image(url, os.path.join(imgs_outpath,f'{img_id}.jpg'))

        # parse the linked pointcloud and put it on the folder:
        cloud_rootpath = find_matching_folderpath(KITTI_rootpath,sequence)

        cloud_path = os.path.join(
            find_folder_recursive(cloud_rootpath,'velodyne_points'),
            'data',
            f'{capture}.bin')
        
        parsed_cloupath = os.path.join(outfolderpath,outname+'.txt')

        parse_pointcloud(cloud_path,parsed_cloupath)

    else:
        shutil.rmtree(outfolderpath)

     

