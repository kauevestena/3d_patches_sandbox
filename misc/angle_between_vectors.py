from lib import *
import numpy as np

# v1 = np.array([-.122946,-.984275,-.126836])
v1 = np.array((-0.0420859 , 0.992 , -0.119013))
v2 = np.array((0.116946 , 0.98569 , -0.121407))
# v2 = np.array([-.020428,.9929912,-.117082])


angle = calculate_angle_between_vectors(v1, v2)
print(f"Angle between vector1 and vector2: {angle} degrees")