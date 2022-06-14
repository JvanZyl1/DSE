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
f_validation = Fuselage(1.2)
# Define CrossSection(z-range, radius-range)
cs_validation = CrossSection([0.0, 1.2], [0.5, 0.5])

# Define booms  ## Cross-section 2
boom_val_0 = Boom(cs_validation.R * np.cos(2 * pi * 0.0), cs_validation.R * np.sin(2 * pi * 0.0), 50e-6, 0.0006)
boom_val_1 = Boom(cs_validation.R * np.cos(2 * pi * 0.1), cs_validation.R * np.sin(2 * pi * 0.1), 50e-6, 0.0006)
boom_val_2 = Boom(cs_validation.R * np.cos(2 * pi * 0.2), cs_validation.R * np.sin(2 * pi * 0.2), 50e-6, 0.0006)
boom_val_3 = Boom(cs_validation.R * np.cos(2 * pi * 0.3), cs_validation.R * np.sin(2 * pi * 0.3), 50e-6, 0.0006)
boom_val_4 = Boom(cs_validation.R * np.cos(2 * pi * 0.4), cs_validation.R * np.sin(2 * pi * 0.4), 50e-6, 0.0006)
boom_val_5 = Boom(cs_validation.R * np.cos(2 * pi * 0.5), cs_validation.R * np.sin(2 * pi * 0.5), 50e-6, 0.0006)
boom_val_6 = Boom(cs_validation.R * np.cos(2 * pi * 0.6), cs_validation.R * np.sin(2 * pi * 0.6), 300e-6, 0.0006)
boom_val_7 = Boom(cs_validation.R * np.cos(2 * pi * 0.7), cs_validation.R * np.sin(2 * pi * 0.7), 600e-6, 0.0006)
boom_val_8 = Boom(cs_validation.R * np.cos(2 * pi * 0.8), cs_validation.R * np.sin(2 * pi * 0.8), 600e-6, 0.0006)
boom_val_9 = Boom(cs_validation.R * np.cos(2 * pi * 0.9), cs_validation.R * np.sin(2 * pi * 0.9), 300e-6, 0.0006)


# Assign booms to cross-sections
cs_validation.add_boom([boom_val_0, boom_val_1, boom_val_2, boom_val_3, boom_val_4,
                        boom_val_5, boom_val_6, boom_val_7, boom_val_8, boom_val_9])


# Assign cross-sections to fuselage
f_validation.add_cs([cs_validation])

"""
Run Following Functions
"""

# fuselage.weight_FL()
f_validation.shear_FL()
f_validation.plot_loads(f_validation.My)
#fuselage.plot_loads(fuselage.Mx_L)
plt.grid(True)
plt.show()
#print(fuselage.Vy(3.501))


print("SHEAR")
for boom in cs_validation.booms:
    print('boom.X, boom.Y', boom.N_B, 'q = ', boom.q, boom.tau_max)
    if abs(boom.tau[0]) <= abs(boom.tau_max[0]) and abs(boom.tau[1]) <= abs(boom.tau_max[1]):
        print('z0 =     OK', 'z1 =     OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    elif abs(boom.tau[0]) > abs(boom.tau_max[0]) and abs(boom.tau[1]) <= abs(boom.tau_max[1]):
        print('z0 = NOT OK', 'z1 =     OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    elif abs(boom.tau[0]) <= abs(boom.tau_max[0]) and abs(boom.tau[1]) > abs(boom.tau_max[1]):
        print('z0 =     OK', 'z1 = NOT OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))
    else:
        print('z0 = NOT OK', 'z1 = NOT OK', boom.tau, np.around(boom.tau / np.array(boom.tau_max) * 100, 5))

print("\nSTRESS")
for boom in cs_validation.booms:
    print('boom.X, boom.Y', boom.N_B, '           ', '           ', boom.sigma_max)
    if abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) > abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) > abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 = NOT OK', boom.sigma_z)
    else:
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 = NOT OK', boom.sigma_z)

cs_validation.plot_booms()
cs_validation.plot_skin(True)
