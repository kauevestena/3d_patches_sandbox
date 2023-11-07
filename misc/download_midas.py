import torch

# model_type = "DPT_Large"

# midas_model = torch.hub.load("intel-isl/MiDaS", model_type)


import torch

torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)