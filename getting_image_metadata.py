from lib import *
import requests

mly.set_access_token(get_mapillary_token())

# img_data = mly.image_from_key(314546700331431)

# img_data = json.loads(img_data)

img_data = get_mly_img_data(314546700331431)

dump_json(img_data, 'image_data.json')



