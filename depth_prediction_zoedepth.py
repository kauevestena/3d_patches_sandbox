from midas_funcs import *

def main():
    basepath = '../sample_mapillary_data/data'

    for folderpath in listdir_fullpath(basepath):
        for itempath in listdir_fullpath(folderpath):
            if 'json' in itempath:
                json_path = itempath

            if 'images' in itempath:
                imgs_path = itempath

        img_metadata = prepare_img_data_dict(json_path)

        # img_id = img_metadata['data'][0]['id']

        # img_f = img_metadata['data'][0]['camera_parameters'][0]

        outfolderpath = os.path.join(folderpath,'zoe_pointclouds')

        create_folder_if_not_exists(outfolderpath)

        for imagepath in listdir_fullpath(imgs_path):
            img_id = get_filename_from_path(imagepath)
            
            if img_id in img_metadata:
                img_f = img_metadata[img_id]['camera_parameters'][0]

                img_type = img_metadata[img_id]['camera_type']

                outpath = os.path.join(outfolderpath,f'{img_id}.txt')

                if img_type == 'perspective':
                    if not os.path.exists(outpath):
                        zoedepth_prediction(imagepath, img_f, outpath)
                        print(outpath)
                else:
                    if os.path.exists(outpath):
                        os.remove(outpath)
                


if __name__ == '__main__':
    main()