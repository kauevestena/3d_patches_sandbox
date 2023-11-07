from lib import *
from PIL import Image

import cv2
import torch
import numpy as np



def midas_predict(filename,f=None,outpath=None):
    model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
    #model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
    #model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

    midas_model = torch.hub.load("intel-isl/MiDaS", model_type)

    device = torch.device("cuda") #if torch.cuda.is_available() else torch.device("cpu")
    midas_model.to(device)
    midas_model.eval()

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

    if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
        transform = midas_transforms.dpt_transform
    else:
        transform = midas_transforms.small_transform

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    input_batch = transform(img).to(device)

    with torch.no_grad():
        prediction = midas_model(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    output = prediction.cpu().numpy()

    if f and outpath:
        save_as_pointcloud(output,img,f, outpath)

    return output

def zoedepth_prediction(filepath,f=None,outpath=None):
    torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)

    image = Image.open(filepath).convert("RGB") 

    repo = "isl-org/ZoeDepth"

    model_zoe_nk = torch.hub.load(repo, "ZoeD_NK", pretrained=True)

    zoe = model_zoe_nk.to('cuda')

    depth_tensor = zoe.infer_pil(image,pad_input=False, output_type="tensor")

    as_np = np.array(depth_tensor)

    if f and outpath:
        save_as_pointcloud(as_np,image,f, outpath)

    return as_np