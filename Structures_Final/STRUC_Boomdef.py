if __name__ == "__main__":
    print("RUN Definition file")

else:
    print("Definition file imported\n\n", __name__)

from STRUC_Class_Crosssection import CrossSection
from STRUC_Class_Boom import Boom
from STRUC_Fuselage import Fuselage

from matplotlib import pyplot as plt
import numpy as np
from math import *

# Define Fuselage(length)
fuselage = Fuselage(3)


# Define CrossSection(z-range, radius-range)
cs_1 = CrossSection([0, 0.5], [0.2, 0.8])
cs_2 = CrossSection([0.5, 1.1], [0.8, 1.1])

# Define booms
boom_1_01 = Boom(cs_1.R * np.cos(2 * pi * 0.1), cs_1.R * np.sin(2 * pi * 0.1), 0.0003, 0.001)
boom_1_02 = Boom(cs_1.R * np.cos(2 * pi * 0.2), cs_1.R * np.sin(2 * pi * 0.2), 0.0003, 0.002)
boom_1_03 = Boom(cs_1.R * np.cos(2 * pi * 0.3), cs_1.R * np.sin(2 * pi * 0.3), 0.0003, 0.001)
boom_1_04 = Boom(cs_1.R * np.cos(2 * pi * 0.4), cs_1.R * np.sin(2 * pi * 0.4), 0.0003, 0.0015)
boom_1_05 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0005, 0.004)
boom_1_06 = Boom(cs_1.R * np.cos(2 * pi * 0.6), cs_1.R * np.sin(2 * pi * 0.6), 0.0003, 0.001)
boom_1_07 = Boom(cs_1.R * np.cos(2 * pi * 0.7), cs_1.R * np.sin(2 * pi * 0.7), 0.0003, 0.001)
boom_1_08 = Boom(cs_1.R * np.cos(2 * pi * 0.8), cs_1.R * np.sin(2 * pi * 0.8), 0.0003, 0.002)
boom_1_09 = Boom(cs_1.R * np.cos(2 * pi * 0.9), cs_1.R * np.sin(2 * pi * 0.9), 0.0003, 0.001)
boom_1_10 = Boom(cs_1.R * np.cos(2 * pi * 1.0), cs_1.R * np.sin(2 * pi * 1.0), 0.0003, 0.0025)

boom_2_01 = Boom(cs_1.R * np.cos(2 * pi * 0.125), cs_1.R * np.sin(2 * pi * 0.125), 0.0003, 0.001)
boom_2_02 = Boom(cs_1.R * np.cos(2 * pi * 0.25), cs_1.R * np.sin(2 * pi * 0.25), 0.0003, 0.002)
boom_2_03 = Boom(cs_1.R * np.cos(2 * pi * 0.375), cs_1.R * np.sin(2 * pi * 0.375), 0.0003, 0.001)
boom_2_04 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0003, 0.0015)
boom_2_05 = Boom(cs_1.R * np.cos(2 * pi * 0.625), cs_1.R * np.sin(2 * pi * 0.625), 0.0005, 0.004)
boom_2_06 = Boom(cs_1.R * np.cos(2 * pi * 0.75), cs_1.R * np.sin(2 * pi * 0.75), 0.0003, 0.001)
boom_2_07 = Boom(cs_1.R * np.cos(2 * pi * 0.875), cs_1.R * np.sin(2 * pi * 0.875), 0.0003, 0.001)
boom_2_08 = Boom(cs_1.R * np.cos(2 * pi * 1), cs_1.R * np.sin(2 * pi * 1), 0.0003, 0.002)

# Assign booms to cross-sections
cs_1.add_boom([boom_1_01, boom_1_02, boom_1_03, boom_1_04, boom_1_05, boom_1_06, boom_1_07, boom_1_08, boom_1_09, boom_1_10])
cs_2.add_boom([boom_2_01, boom_2_02, boom_2_03, boom_2_04, boom_2_05, boom_2_06, boom_2_07, boom_2_08])

# Assign cross-sections to fuselage
fuselage.add_cs([cs_1, cs_2])

fuselage.weight_FL()
fuselage.stress_FL()




