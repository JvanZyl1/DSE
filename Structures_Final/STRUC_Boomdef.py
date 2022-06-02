from STRUC_Classes import CrossSection, Boom
from STRUC_Fuselage import FuselageLoads
from matplotlib import pyplot as plt
import numpy as np
from math import *

fuselage = FuselageLoads(0.1)
cs_1 = CrossSection(np.array([0, 0.5]), np.array([0.2, 0.8]))
boom_1_1 = Boom(cs_1.radius * np.cos(2 * pi * 0.1), cs_1.radius * np.sin(2 * pi * 0.1), 0.00003, 0.001)
boom_1_2 = Boom(cs_1.radius * np.cos(2 * pi * 0.2), cs_1.radius * np.sin(2 * pi * 0.2), 0.00003, 0.002)
boom_1_3 = Boom(cs_1.radius * np.cos(2 * pi * 0.3), cs_1.radius * np.sin(2 * pi * 0.3), 0.00003, 0.001)
boom_1_4 = Boom(cs_1.radius * np.cos(2 * pi * 0.4), cs_1.radius * np.sin(2 * pi * 0.4), 0.00003, 0.0015)
boom_1_5 = Boom(cs_1.radius * np.cos(2 * pi * 0.5), cs_1.radius * np.sin(2 * pi * 0.5), 0.00005, 0.004)
boom_1_6 = Boom(cs_1.radius * np.cos(2 * pi * 0.6), cs_1.radius * np.sin(2 * pi * 0.6), 0.00003, 0.001)
boom_1_7 = Boom(cs_1.radius * np.cos(2 * pi * 0.7), cs_1.radius * np.sin(2 * pi * 0.7), 0.00003, 0.001)
boom_1_8 = Boom(cs_1.radius * np.cos(2 * pi * 0.8), cs_1.radius * np.sin(2 * pi * 0.8), 0.00003, 0.002)
boom_1_9 = Boom(cs_1.radius * np.cos(2 * pi * 0.9), cs_1.radius * np.sin(2 * pi * 0.9), 0.00003, 0.001)
boom_1_10 = Boom(cs_1.radius * np.cos(2 * pi * 1.0), cs_1.radius * np.sin(2 * pi * 1.0), 0.00003, 0.0025)
cs_1.add_boom([boom_1_1, boom_1_2, boom_1_3, boom_1_4, boom_1_5, boom_1_6, boom_1_7, boom_1_8, boom_1_9, boom_1_10])

print(cs_1.Ixx_cs())
