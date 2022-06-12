if __name__ == "__main__":
    pass  # print("RUN Definition file")
else:
    pass  # print("Definition file imported\n\n", __name__)

from STRUC_Class_Crosssection import CrossSection
from STRUC_Class_Boom import Boom
from STRUC_Fuselage import Fuselage

from matplotlib import pyplot as plt
import numpy as np
from math import *

# Define Fuselage(length)
fuselage = Fuselage(3.501)
# Define CrossSection(z-range, radius-range)
cs_1 = CrossSection([0.100, 0.622], [0.280, 0.301])
cs_2 = CrossSection([0.622, 1.000], [0.301, 0.412])
cs_3 = CrossSection([1.000, 1.503], [0.412, 0.487])
cs_4 = CrossSection([1.503, 2.301], [0.487, 0.551])
cs_5 = CrossSection([2.301, 2.800], [0.551, 0.562])
cs_6 = CrossSection([2.800, 3.500], [0.562, 0.303])

# Define booms  ## Cross-section 1
boom_1_01 = Boom(cs_1.R * np.cos(2 * pi * 0.121), cs_1.R * np.sin(2 * pi * 0.121), 3e-6, 0.0006)
boom_1_02 = Boom(cs_1.R * np.cos(2 * pi * 0.379), cs_1.R * np.sin(2 * pi * 0.379), 3e-6, 0.0006)
boom_1_03 = Boom(cs_1.R * np.cos(2 * pi * 0.596), cs_1.R * np.sin(2 * pi * 0.596), 3e-6, 0.0006)
boom_1_04 = Boom(cs_1.R * np.cos(2 * pi * 0.695), cs_1.R * np.sin(2 * pi * 0.695), 3e-6, 0.0006)
boom_1_05 = Boom(cs_1.R * np.cos(2 * pi * 0.805), cs_1.R * np.sin(2 * pi * 0.805), 3e-6, 0.0006)
boom_1_06 = Boom(cs_1.R * np.cos(2 * pi * 0.904), cs_1.R * np.sin(2 * pi * 0.904), 3e-6, 0.0006)

# Define booms  ## Cross-section 2
boom_2_01 = Boom(cs_1.R * np.cos(2 * pi * 0.121), cs_1.R * np.sin(2 * pi * 0.121), 3e-6, 0.0006)
boom_2_02 = Boom(cs_1.R * np.cos(2 * pi * 0.379), cs_1.R * np.sin(2 * pi * 0.379), 3e-6, 0.0006)
boom_2_03 = Boom(cs_1.R * np.cos(2 * pi * 0.596), cs_1.R * np.sin(2 * pi * 0.596), 3e-6, 0.0006)
boom_2_04 = Boom(cs_1.R * np.cos(2 * pi * 0.641), cs_1.R * np.sin(2 * pi * 0.641), 3e-6, 0.0006)
boom_2_05 = Boom(cs_1.R * np.cos(2 * pi * 0.750), cs_1.R * np.sin(2 * pi * 0.750), 3e-6, 0.0006)
boom_2_06 = Boom(cs_1.R * np.cos(2 * pi * 0.859), cs_1.R * np.sin(2 * pi * 0.859), 3e-6, 0.0006)
boom_2_07 = Boom(cs_1.R * np.cos(2 * pi * 0.904), cs_1.R * np.sin(2 * pi * 0.904), 3e-6, 0.0006)

# Define booms  ## Cross-section 3
boom_3_01 = Boom(cs_1.R * np.cos(2 * pi * 0.121), cs_1.R * np.sin(2 * pi * 0.121), 3e-6, 0.000)
boom_3_02 = Boom(cs_1.R * np.cos(2 * pi * 0.379), cs_1.R * np.sin(2 * pi * 0.379), 3e-6, 0.000)
boom_3_03 = Boom(cs_1.R * np.cos(2 * pi * 0.596), cs_1.R * np.sin(2 * pi * 0.596), 3e-6, 0.000)
boom_3_04 = Boom(cs_1.R * np.cos(2 * pi * 0.641), cs_1.R * np.sin(2 * pi * 0.641), 3e-6, 0.001)
boom_3_05 = Boom(cs_1.R * np.cos(2 * pi * 0.710), cs_1.R * np.sin(2 * pi * 0.710), 3e-6, 0.001)
boom_3_06 = Boom(cs_1.R * np.cos(2 * pi * 0.790), cs_1.R * np.sin(2 * pi * 0.790), 3e-6, 0.001)
boom_3_07 = Boom(cs_1.R * np.cos(2 * pi * 0.859), cs_1.R * np.sin(2 * pi * 0.859), 3e-6, 0.000)
boom_3_08 = Boom(cs_1.R * np.cos(2 * pi * 0.904), cs_1.R * np.sin(2 * pi * 0.904), 3e-6, 0.000)

# Define booms  ## Cross-section 4
boom_4_01 = Boom(cs_1.R * np.cos(2 * pi * 0.122), cs_1.R * np.sin(2 * pi * 0.122), 3e-6, 0.000)
boom_4_02 = Boom(cs_1.R * np.cos(2 * pi * 0.152), cs_1.R * np.sin(2 * pi * 0.152), 3e-6, 0.001)
boom_4_03 = Boom(cs_1.R * np.cos(2 * pi * 0.250), cs_1.R * np.sin(2 * pi * 0.250), 3e-6, 0.001)
boom_4_04 = Boom(cs_1.R * np.cos(2 * pi * 0.348), cs_1.R * np.sin(2 * pi * 0.348), 3e-6, 0.000)
boom_4_05 = Boom(cs_1.R * np.cos(2 * pi * 0.378), cs_1.R * np.sin(2 * pi * 0.378), 3e-6, 0.000)
boom_4_06 = Boom(cs_1.R * np.cos(2 * pi * 0.617), cs_1.R * np.sin(2 * pi * 0.617), 3e-6, 0.000)
boom_4_07 = Boom(cs_1.R * np.cos(2 * pi * 0.641), cs_1.R * np.sin(2 * pi * 0.641), 3e-6, 0.002)
boom_4_08 = Boom(cs_1.R * np.cos(2 * pi * 0.710), cs_1.R * np.sin(2 * pi * 0.710), 3e-6, 0.001)
boom_4_09 = Boom(cs_1.R * np.cos(2 * pi * 0.790), cs_1.R * np.sin(2 * pi * 0.790), 3e-6, 0.001)
boom_4_10 = Boom(cs_1.R * np.cos(2 * pi * 0.859), cs_1.R * np.sin(2 * pi * 0.859), 3e-6, 0.000)
boom_4_11 = Boom(cs_1.R * np.cos(2 * pi * 0.883), cs_1.R * np.sin(2 * pi * 0.883), 3e-6, 0.000)


# Define booms  ## Cross-section 5
boom_5_01 = Boom(cs_1.R * np.cos(2 * pi * 0.022), cs_1.R * np.sin(2 * pi * 0.022), 3e-6, 0.001)
boom_5_02 = Boom(cs_1.R * np.cos(2 * pi * 0.125), cs_1.R * np.sin(2 * pi * 0.125), 3e-6, 0.002)
boom_5_03 = Boom(cs_1.R * np.cos(2 * pi * 0.250), cs_1.R * np.sin(2 * pi * 0.250), 3e-6, 0.001)
boom_5_04 = Boom(cs_1.R * np.cos(2 * pi * 0.375), cs_1.R * np.sin(2 * pi * 0.375), 3e-6, 0.001)
boom_5_05 = Boom(cs_1.R * np.cos(2 * pi * 0.478), cs_1.R * np.sin(2 * pi * 0.478), 3e-6, 0.0015)
boom_5_06 = Boom(cs_1.R * np.cos(2 * pi * 0.550), cs_1.R * np.sin(2 * pi * 0.550), 3e-6, 0.001)
boom_5_07 = Boom(cs_1.R * np.cos(2 * pi * 0.637), cs_1.R * np.sin(2 * pi * 0.637), 3e-6, 0.002)
boom_5_08 = Boom(cs_1.R * np.cos(2 * pi * 0.710), cs_1.R * np.sin(2 * pi * 0.710), 3e-6, 0.001)
boom_5_09 = Boom(cs_1.R * np.cos(2 * pi * 0.790), cs_1.R * np.sin(2 * pi * 0.790), 3e-6, 0.001)
boom_5_10 = Boom(cs_1.R * np.cos(2 * pi * 0.875), cs_1.R * np.sin(2 * pi * 0.875), 3e-6, 0.0015)
boom_5_11 = Boom(cs_1.R * np.cos(2 * pi * 0.950), cs_1.R * np.sin(2 * pi * 0.950), 3e-6, 0.001)

# Define booms  ## Cross-section 5
boom_6_01 = Boom(cs_1.R * np.cos(2 * pi * 0.022), cs_1.R * np.sin(2 * pi * 0.022), 3e-6, 0.000)
boom_6_02 = Boom(cs_1.R * np.cos(2 * pi * 0.250), cs_1.R * np.sin(2 * pi * 0.250), 3e-6, 0.000)
boom_6_03 = Boom(cs_1.R * np.cos(2 * pi * 0.478), cs_1.R * np.sin(2 * pi * 0.478), 3e-6, 0.0006)
boom_6_04 = Boom(cs_1.R * np.cos(2 * pi * 0.550), cs_1.R * np.sin(2 * pi * 0.550), 3e-6, 0.0006)
boom_6_05 = Boom(cs_1.R * np.cos(2 * pi * 0.637), cs_1.R * np.sin(2 * pi * 0.637), 3e-6, 0.0006)
boom_6_06 = Boom(cs_1.R * np.cos(2 * pi * 0.750), cs_1.R * np.sin(2 * pi * 0.750), 3e-6, 0.0006)
boom_6_07 = Boom(cs_1.R * np.cos(2 * pi * 0.875), cs_1.R * np.sin(2 * pi * 0.875), 3e-6, 0.0006)
boom_6_08 = Boom(cs_1.R * np.cos(2 * pi * 0.950), cs_1.R * np.sin(2 * pi * 0.950), 3e-6, 0.0006)

# Assign booms to cross-sections
cs_1.add_boom([boom_1_01, boom_1_02, boom_1_03, boom_1_04, boom_1_05,
               boom_1_06])
cs_2.add_boom([boom_2_01, boom_2_02, boom_2_03,
               boom_2_04, boom_2_05, boom_2_06, boom_2_07])
cs_3.add_boom([boom_3_01, boom_3_02, boom_3_03, boom_3_04, boom_3_05,
               boom_3_06, boom_3_07, boom_3_08])
cs_4.add_boom([boom_4_01, boom_4_02, boom_4_03, boom_4_04, boom_4_05,
               boom_4_06, boom_4_07, boom_4_08, boom_4_09, boom_4_10, boom_4_11])
cs_5.add_boom([boom_5_01, boom_5_02, boom_5_03, boom_5_04, boom_5_05,
               boom_5_06, boom_5_07, boom_5_08, boom_5_09, boom_5_10, boom_5_11])
cs_6.add_boom([boom_6_01, boom_6_02, boom_6_03, boom_6_04, boom_6_05, boom_6_06, boom_6_07, boom_6_08])

# Assign cross-sections to fuselage
fuselage.add_cs([cs_1, cs_2, cs_3,
                 cs_4, cs_5, cs_6])

"""
Run Following Functions
"""
# fuselage.weight_FL()
fuselage.shear_FL()
# fuselage.plot_loads(fuselage.Vy, True)
# print(fuselage.Vy(3.501))
cs_4.plot_booms()
cs_4.plot_skin(True)
