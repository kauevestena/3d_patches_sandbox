from lib import *
import zlib
import requests

img_data = read_json('image_data.json')

sfm_url = img_data['features']['properties']['sfm_cluster']['url']


sfm_url = "https://scontent-mxp2-1.xx.fbcdn.net/m1/v/t0.40383-6/An_6Kmz_PMlmrq3wVYiwSqYsiSLsxpPDJw86xMPRAWjZOyzxPZbSqeBuch92nivrNG9mG1IxJDbF169lZnNpcyzN4Bvm82wI9mAPB_yQGz5qt4wpzOAi0RWGOKfK14mLvG13BZMVOteSoA?ccb=10-5&oh=00_AfBHnmHq59G8QGxjPXv224g4kJh2D0maCWdgQbbUQ9_D8Q&oe=6554B5E7&_nc_sid=fbd883"

response = requests.get(sfm_url)
content = response.content

data = json.loads(zlib.decompress(content).decode('utf-8'))

dump_json(data,'sfm_cluster.json')