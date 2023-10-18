from lib import *
import numpy as np

# v1 = np.array([-.122946,-.984275,-.126836])
v1 = np.array([-.023078,.992684,-.118513])
v2 = np.array([.096724,.989094,-.111071])
# v2 = np.array([-.020428,.9929912,-.117082])


angle = calculate_angle_between_vectors(v1, v2)
print(f"Angle between vector1 and vector2: {angle} degrees")