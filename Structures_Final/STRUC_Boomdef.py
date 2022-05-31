from STRUC_Classes import CrossSection, Boom
from matplotlib import pyplot as plt
import numpy as np
from math import *

cs_1 = CrossSection(0, 0, np.array([0, 0.5]), np.array([0.2, 0.8]))
cs_1.print_booms()
boom_1_1 = Boom(cs_1.radius * np.sin(2 * pi * 0.1), cs_1.radius * np.cos(2 * pi * 0.1))
boom_1_2 = Boom(cs_1.radius * np.sin(2 * pi * 0.2), cs_1.radius * np.cos(2 * pi * 0.2))
boom_1_3 = Boom(cs_1.radius * np.sin(2 * pi * 0.3), cs_1.radius * np.cos(2 * pi * 0.3))
boom_1_4 = Boom(cs_1.radius * np.sin(2 * pi * 0.4), cs_1.radius * np.cos(2 * pi * 0.4))
boom_1_5 = Boom(cs_1.radius * np.sin(2 * pi * 0.5), cs_1.radius * np.cos(2 * pi * 0.5))
boom_1_6 = Boom(cs_1.radius * np.sin(2 * pi * 0.6), cs_1.radius * np.cos(2 * pi * 0.6))
boom_1_7 = Boom(cs_1.radius * np.sin(2 * pi * 0.7), cs_1.radius * np.cos(2 * pi * 0.7))
boom_1_8 = Boom(cs_1.radius * np.sin(2 * pi * 0.8), cs_1.radius * np.cos(2 * pi * 0.8))
boom_1_9 = Boom(cs_1.radius * np.sin(2 * pi * 0.9), cs_1.radius * np.cos(2 * pi * 0.9))
boom_1_10 = Boom(cs_1.radius * np.sin(2 * pi * 1.0), cs_1.radius * np.cos(2 * pi * 1.0))
cs_1.add_boom([boom_1_1, boom_1_2, boom_1_3, boom_1_4, boom_1_5, boom_1_6, boom_1_7, boom_1_8, boom_1_9, boom_1_10])

cs_1.print_booms()
cs_1.plot_booms()