from lib import *
import numpy as np

v1 = np.array([-.147101,-.977984,.148015])
v2 = np.array([-.026711,.993738,-.108495])


angle = calculate_angle_between_vectors(v1, v2)
print(f"Angle between vector1 and vector2: {angle} degrees")