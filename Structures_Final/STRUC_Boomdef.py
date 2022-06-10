if __name__ == "__main__":
    pass #print("RUN Definition file")

else:
    pass #print("Definition file imported\n\n", __name__)

from STRUC_Class_Crosssection import CrossSection
from STRUC_Class_Boom import Boom
from STRUC_Fuselage import Fuselage

from matplotlib import pyplot as plt
import numpy as np
from math import *

# Define Fuselage(length)
fuselage = Fuselage(3.501)
# Define CrossSection(z-range, radius-range)
cs_1 = CrossSection([0.100, 0.622], [0.560, 0.601])
cs_2 = CrossSection([0.622, 1.000], [0.601, 0.823])
cs_3 = CrossSection([1.000, 2.301], [0.823, 1.102])
cs_4 = CrossSection([2.301, 2.800], [1.102, 1.124])

# Define booms  ## Cross-section 1
boom_1_01 = Boom(cs_1.R * np.cos(2 * pi * 0.1), cs_1.R * np.sin(2 * pi * 0.1), 0.0003, 0.001)
boom_1_02 = Boom(cs_1.R * np.cos(2 * pi * 0.2), cs_1.R * np.sin(2 * pi * 0.2), 0.0003, 0.002)
boom_1_03 = Boom(cs_1.R * np.cos(2 * pi * 0.3), cs_1.R * np.sin(2 * pi * 0.3), 0.0003, 0.001)
boom_1_04 = Boom(cs_1.R * np.cos(2 * pi * 0.4), cs_1.R * np.sin(2 * pi * 0.4), 0.0003, 0.0015)
boom_1_05 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0003, 0.000)
boom_1_06 = Boom(cs_1.R * np.cos(2 * pi * 0.6), cs_1.R * np.sin(2 * pi * 0.6), 0.0003, 0.001)
boom_1_07 = Boom(cs_1.R * np.cos(2 * pi * 0.7), cs_1.R * np.sin(2 * pi * 0.7), 0.0003, 0.001)
boom_1_08 = Boom(cs_1.R * np.cos(2 * pi * 0.8), cs_1.R * np.sin(2 * pi * 0.8), 0.0003, 0.001)
boom_1_09 = Boom(cs_1.R * np.cos(2 * pi * 0.9), cs_1.R * np.sin(2 * pi * 0.9), 0.0003, 0.000)
boom_1_10 = Boom(cs_1.R * np.cos(2 * pi * 1.0), cs_1.R * np.sin(2 * pi * 1.0), 0.0003, 0.0025)

# Define booms  ## Cross-section 2
boom_2_01 = Boom(cs_1.R * np.cos(2 * pi * 0.125), cs_1.R * np.sin(2 * pi * 0.125), 0.0003, 0.001)
boom_2_02 = Boom(cs_1.R * np.cos(2 * pi * 0.25), cs_1.R * np.sin(2 * pi * 0.25), 0.0003, 0.002)
boom_2_03 = Boom(cs_1.R * np.cos(2 * pi * 0.375), cs_1.R * np.sin(2 * pi * 0.375), 0.0003, 0.001)
boom_2_04 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0003, 0.000)
boom_2_05 = Boom(cs_1.R * np.cos(2 * pi * 0.625), cs_1.R * np.sin(2 * pi * 0.625), 0.0005, 0.004)
boom_2_06 = Boom(cs_1.R * np.cos(2 * pi * 0.75), cs_1.R * np.sin(2 * pi * 0.75), 0.0003, 0.001)
boom_2_07 = Boom(cs_1.R * np.cos(2 * pi * 0.875), cs_1.R * np.sin(2 * pi * 0.875), 0.0003, 0.001)
boom_2_08 = Boom(cs_1.R * np.cos(2 * pi * 1), cs_1.R * np.sin(2 * pi * 1), 0.0003, 0.002)

# Define booms  ## Cross-section 3
boom_3_01 = Boom(cs_1.R * np.cos(2 * pi * 0.25), cs_1.R * np.sin(2 * pi * 0.25), 0.0003, 0.001)
boom_3_02 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0003, 0.002)
boom_3_03 = Boom(cs_1.R * np.cos(2 * pi * 0.7), cs_1.R * np.sin(2 * pi * 0.7), 0.0003, 0.001)
boom_3_04 = Boom(cs_1.R * np.cos(2 * pi * 1.00), cs_1.R * np.sin(2 * pi * 1.00), 0.0003, 0.0015)

# Define booms  ## Cross-section 3
boom_4_01 = Boom(cs_1.R * np.cos(2 * pi * 0.25), cs_1.R * np.sin(2 * pi * 0.25), 0.0003, 0.001)
boom_4_02 = Boom(cs_1.R * np.cos(2 * pi * 0.5), cs_1.R * np.sin(2 * pi * 0.5), 0.0003, 0.002)
boom_4_03 = Boom(cs_1.R * np.cos(2 * pi * 0.7), cs_1.R * np.sin(2 * pi * 0.7), 0.0003, 0.001)
boom_4_04 = Boom(cs_1.R * np.cos(2 * pi * 1.00), cs_1.R * np.sin(2 * pi * 1.00), 0.0003, 0.0015)


# Assign booms to cross-sections
cs_1.add_boom([boom_1_01, boom_1_02, boom_1_03, boom_1_04, boom_1_05, boom_1_06, boom_1_07, boom_1_08, boom_1_09, boom_1_10])
cs_2.add_boom([boom_2_01, boom_2_02, boom_2_03, boom_2_04, boom_2_05, boom_2_06, boom_2_07, boom_2_08])
cs_3.add_boom([boom_3_01, boom_3_02, boom_3_03, boom_3_04])
cs_4.add_boom([boom_4_01, boom_4_02, boom_4_03, boom_4_04])
# Assign cross-sections to fuselage
fuselage.add_cs([cs_1, cs_2, cs_3, cs_4])
#fuselage.weight_FL()
#fuselage.plot_loads(fuselage.My, True)
#print(fuselage.Vy(3.501))
fuselage.plot_cs()