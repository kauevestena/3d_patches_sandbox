import pcl

# with open('cloud_small_sample.xyz','r') as reader:  
#     pcl.PointCloud.from_file(reader)

pc = pcl.load_XYZRGB('cloud_small_sample.xyz')