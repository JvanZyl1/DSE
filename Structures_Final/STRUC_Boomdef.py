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
boom_1_01 = Boom(cs_1.R * np.cos(2 * pi * 0.121), cs_1.R * np.sin(2 * pi * 0.121), 60e-6, 0.0002)
boom_1_02 = Boom(cs_1.R * np.cos(2 * pi * 0.250), cs_1.R * np.sin(2 * pi * 0.250), 60e-6, 0.0002)
boom_1_03 = Boom(cs_1.R * np.cos(2 * pi * 0.379), cs_1.R * np.sin(2 * pi * 0.379), 60e-6, 0.0002)
boom_1_04 = Boom(cs_1.R * np.cos(2 * pi * 0.596), cs_1.R * np.sin(2 * pi * 0.596), 50e-6, 0.0002)
boom_1_05 = Boom(cs_1.R * np.cos(2 * pi * 0.695), cs_1.R * np.sin(2 * pi * 0.695), 130e-6, 0.0002)
boom_1_06 = Boom(cs_1.R * np.cos(2 * pi * 0.750), cs_1.R * np.sin(2 * pi * 0.750), 140e-6, 0.0002)
boom_1_07 = Boom(cs_1.R * np.cos(2 * pi * 0.805), cs_1.R * np.sin(2 * pi * 0.805), 130e-6, 0.0002)
boom_1_08 = Boom(cs_1.R * np.cos(2 * pi * 0.904), cs_1.R * np.sin(2 * pi * 0.904), 50e-6, 0.0002)

# Define booms  ## Cross-section 2
boom_2_01 = Boom(cs_2.R * np.cos(2 * pi * 0.121), cs_2.R * np.sin(2 * pi * 0.121), 50e-6, 0.0003)
boom_2_02 = Boom(cs_2.R * np.cos(2 * pi * 0.250), cs_2.R * np.sin(2 * pi * 0.250), 50e-6, 0.0003)
boom_2_03 = Boom(cs_2.R * np.cos(2 * pi * 0.379), cs_2.R * np.sin(2 * pi * 0.379), 50e-6, 0.0003)
boom_2_04 = Boom(cs_2.R * np.cos(2 * pi * 0.596), cs_2.R * np.sin(2 * pi * 0.596), 60e-6, 0.0003)
boom_2_05 = Boom(cs_2.R * np.cos(2 * pi * 0.641), cs_2.R * np.sin(2 * pi * 0.641), 100e-6, 0.0003)
boom_2_06 = Boom(cs_2.R * np.cos(2 * pi * 0.750), cs_2.R * np.sin(2 * pi * 0.750), 110e-6, 0.0003)
boom_2_07 = Boom(cs_2.R * np.cos(2 * pi * 0.859), cs_2.R * np.sin(2 * pi * 0.859), 100e-6, 0.0003)
boom_2_08 = Boom(cs_2.R * np.cos(2 * pi * 0.904), cs_2.R * np.sin(2 * pi * 0.904), 60e-6, 0.0003)

# Define booms  ## Cross-section 3
boom_3_01 = Boom(cs_3.R * 1.1 * np.cos(2 * pi * 0.121), cs_3.R * 1.1 * np.sin(2 * pi * 0.121), 90e-6, 0.000)
boom_3_02 = Boom(cs_3.R * 1.1 * np.cos(2 * pi * 0.379), cs_3.R * 1.1 * np.sin(2 * pi * 0.379), 90e-6, 0.000)
boom_3_03 = Boom(cs_3.R * np.cos(2 * pi * 0.596), cs_3.R * np.sin(2 * pi * 0.596), 300e-6, 0.000)
boom_3_04 = Boom(cs_3.R * np.cos(2 * pi * 0.641), cs_3.R * np.sin(2 * pi * 0.641), 300e-6, 0.0003)
boom_3_05 = Boom(cs_3.R * np.cos(2 * pi * 0.710), cs_3.R * np.sin(2 * pi * 0.710), 200e-6, 0.0003)
boom_3_06 = Boom(cs_3.R * np.cos(2 * pi * 0.790), cs_3.R * np.sin(2 * pi * 0.790), 200e-6, 0.0003)
boom_3_07 = Boom(cs_3.R * np.cos(2 * pi * 0.859), cs_3.R * np.sin(2 * pi * 0.859), 300e-6, 0.000)
boom_3_08 = Boom(cs_3.R * np.cos(2 * pi * 0.904), cs_3.R * np.sin(2 * pi * 0.904), 300e-6, 0.000)

# Define booms  ## Cross-section 4
boom_4_01 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.122), cs_4.R * 1.05 * np.sin(2 * pi * 0.122), 50e-6, 0.000)
boom_4_02 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.152), cs_4.R * 1.05 * np.sin(2 * pi * 0.152), 25e-6, 0.0006)
boom_4_03 = Boom(cs_4.R * np.cos(2 * pi * 0.250), cs_4.R * np.sin(2 * pi * 0.250), 20e-6, 0.0006)
boom_4_04 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.348), cs_4.R * 1.05 * np.sin(2 * pi * 0.348), 25e-6, 0.000)
boom_4_05 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.378), cs_4.R * 1.05 * np.sin(2 * pi * 0.378), 50e-6, 0.000)
boom_4_06 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.617), cs_4.R * 1.05 * np.sin(2 * pi * 0.617), 100e-6, 0.000)
boom_4_07 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.641), cs_4.R * 1.05 * np.sin(2 * pi * 0.641), 70e-6, 0.0006)
boom_4_08 = Boom(cs_4.R * np.cos(2 * pi * 0.710), cs_4.R * np.sin(2 * pi * 0.710), 5e-6, 0.0006)
boom_4_09 = Boom(cs_4.R * np.cos(2 * pi * 0.790), cs_4.R * np.sin(2 * pi * 0.790), 5e-6, 0.0006)
boom_4_10 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.859), cs_4.R * 1.05 * np.sin(2 * pi * 0.859), 70e-6, 0.000)
boom_4_11 = Boom(cs_4.R * 1.05 * np.cos(2 * pi * 0.883), cs_4.R * 1.05 * np.sin(2 * pi * 0.883), 100e-6, 0.000)

# Define booms  ## Cross-section 5
boom_5_01 = Boom(cs_5.R * np.cos(2 * pi * 0.022), cs_5.R * np.sin(2 * pi * 0.022), 10e-6, 0.0006)
boom_5_02 = Boom(cs_5.R * np.cos(2 * pi * 0.125), cs_5.R * np.sin(2 * pi * 0.125), 25e-6, 0.0006)
boom_5_03 = Boom(cs_5.R * np.cos(2 * pi * 0.250), cs_5.R * np.sin(2 * pi * 0.250), 15e-6, 0.0006)
boom_5_04 = Boom(cs_5.R * np.cos(2 * pi * 0.375), cs_5.R * np.sin(2 * pi * 0.375), 25e-6, 0.0006)
boom_5_05 = Boom(cs_5.R * np.cos(2 * pi * 0.478), cs_5.R * np.sin(2 * pi * 0.478), 10e-6, 0.000)
boom_5_06 = Boom(cs_5.R * np.cos(2 * pi * 0.637), cs_5.R * np.sin(2 * pi * 0.637), 30e-6, 0.0006)
boom_5_07 = Boom(cs_5.R * np.cos(2 * pi * 0.710), cs_5.R * np.sin(2 * pi * 0.710), 20e-6, 0.0006)
boom_5_08 = Boom(cs_5.R * np.cos(2 * pi * 0.790), cs_5.R * np.sin(2 * pi * 0.790), 20e-6, 0.0006)
boom_5_09 = Boom(cs_5.R * np.cos(2 * pi * 0.875), cs_5.R * np.sin(2 * pi * 0.875), 30e-6, 0.000)

# Define booms  ## Cross-section 5
boom_6_01 = Boom(cs_6.R * np.cos(2 * pi * 0.022), cs_6.R * np.sin(2 * pi * 0.022), 3e-6, 0.000)
boom_6_02 = Boom(cs_6.R * np.cos(2 * pi * 0.250), cs_6.R * np.sin(2 * pi * 0.250), 30e-6, 0.000)
boom_6_03 = Boom(cs_6.R * np.cos(2 * pi * 0.478), cs_6.R * np.sin(2 * pi * 0.478), 3e-6, 0.0006)
boom_6_04 = Boom(cs_6.R * np.cos(2 * pi * 0.550), cs_6.R * np.sin(2 * pi * 0.550), 3e-6, 0.0006)
boom_6_05 = Boom(cs_6.R * np.cos(2 * pi * 0.637), cs_6.R * np.sin(2 * pi * 0.637), 3e-6, 0.0006)
boom_6_06 = Boom(cs_6.R * np.cos(2 * pi * 0.750), cs_6.R * np.sin(2 * pi * 0.750), 3e-6, 0.0006)
boom_6_07 = Boom(cs_6.R * np.cos(2 * pi * 0.875), cs_6.R * np.sin(2 * pi * 0.875), 3e-6, 0.0006)
boom_6_08 = Boom(cs_6.R * np.cos(2 * pi * 0.950), cs_6.R * np.sin(2 * pi * 0.950), 3e-6, 0.0006)

# Assign booms to cross-sections
cs_1.add_boom([boom_1_01, boom_1_02, boom_1_03, boom_1_04, boom_1_05,
               boom_1_06, boom_1_07, boom_1_08])
cs_2.add_boom([boom_2_01, boom_2_02, boom_2_03,
               boom_2_04, boom_2_05, boom_2_06, boom_2_07, boom_2_08])
cs_3.add_boom([boom_3_01, boom_3_02, boom_3_03, boom_3_04, boom_3_05,
               boom_3_06, boom_3_07, boom_3_08])
cs_4.add_boom([boom_4_01, boom_4_02, boom_4_03, boom_4_04, boom_4_05,
               boom_4_06, boom_4_07, boom_4_08, boom_4_09, boom_4_10, boom_4_11])
cs_5.add_boom([boom_5_01, boom_5_02, boom_5_03, boom_5_04, boom_5_05,
               boom_5_06, boom_5_07, boom_5_08, boom_5_09])
cs_6.add_boom([boom_6_01, boom_6_02, boom_6_03, boom_6_04, boom_6_05, boom_6_06, boom_6_07, boom_6_08])

# Assign cross-sections to fuselage
fuselage.add_cs([cs_1, cs_2, cs_3,
                 cs_4, cs_5, cs_6])
fuselage.shear_FL()
"""
Run Following Functions


# fuselage.weight_FL()
fuselage.shear_FL()
fuselage.plot_loads(fuselage.Vy)

plt.grid(True)
plt.savefig('Load_Diagram_verification.png')
plt.show()
"""
#print(fuselage.Vy(3.501))
cs = cs_3
print('Boom', '\t&', '$x$ ', '\t&', '$y$ ', '\t& ', r'$B$ ','\t& ', r'$t_{\textrm{D}}$ ', '\t\t&',r'$\Delta I_{xx}$ ','\t&', r'$\Delta I_{yy}$',
      '\t&', r'$\bar{\sigma}_z$ ', '\t&', r'$\bar{\sigma}_{\textrm{cr}}$ ',
'\t&', r'$\bar{\tau}$ ', '\t&', r'$\bar{\tau}_{\textrm{cr}}$ ',
      r'\\')
print('\t\t&', '[m]','\t&', '[m]', '\t& ',
      r'[\unit{mm^2}]','\t&', '[mm]', '\t&',r'[\unit{m^4}]','\t&', r' [\unit{m^4}]',
      '\t&', r' [MPa]', '\t&', r'[MPa]', '\t&', r' [MPa]', '\t&', r'[MPa]',
      r'\\ \hline')

for boom in cs.booms:
    print(boom.N_B + 1, '\t\t&', round(boom.X[0], 3), '  \t&', round(boom.Y[0], 3), '  \t&',
          boom.B[0] * 1e6, ' \t&', str(boom.t*1e3), '\t&', '$' + str(round(boom.B[0] * boom.Y[0]**2*1e6, 2)) + 'e6$',
          ' \t\t&', '$' + str(round(boom.B[0] * boom.X[0]**2*1e6, 2)) + 'e6$', '\t\t\t&',
          round(boom.sigma_z[0]/1e6, 1), ' \t\t\t\t\t&', round(boom.sigma_cr[0]/1e6, 1), '\t\t\t\t&',
          round(boom.tau[0] / 1e6, 1), ' \t\t\t\t\t&', round(boom.tau_cr[0] / 1e6, 1),
          r'\\')

    print(' ', '\t\t&', round(boom.X[1], 3), '  \t&', round(boom.Y[1], 3), '  \t&',
          ' \t\t\t&',' \t\t&', '$' + str(round(boom.B[1] * boom.Y[1]**2*1e6, 2)) + 'e6$',
          ' \t\t&', '$' + str(round(boom.B[1] * boom.X[1]**2*1e6, 2)) + 'e6$', '\t\t\t&',
          round(boom.sigma_z[1]/1e6, 1), ' \t\t\t\t\t&', round(boom.sigma_cr[0]/1e6, 1), '\t\t\t\t&',
          round(boom.tau[1] / 1e6, 1), ' \t\t\t\t\t&', round(boom.tau_cr[0] / 1e6, 1),
          r'\\ \hline')

print('Boom', '\t&', '$A$ ',
      r'\\')
print('\t\t&', r'[\unit{m^2}]',
      r'\\ \hline')
cs.boom_area()
for boom in cs.booms:
    print(boom.N_B + 1, '\t\t&', '$' + str(round(boom.A[0]*1e5, 3))+ 'e5$','\t\t&', boom.weight_boom(),
          r'\\')

    print(' ', '\t\t&', '$' + str(round(boom.A[1]*1e5, 3))+ 'e5$',
          r'\\ \hline')









"""
print("SHEAR")
for boom in cs.booms:
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
for boom in cs.booms:
    print('boom.X, boom.Y', boom.N_B, '           ', '           ', boom.sigma_max)
    if abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) > abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) <= abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 =     OK', boom.sigma_z)
    elif abs(boom.sigma_z[0]) <= abs(boom.sigma_max[0]) and abs(boom.sigma_z[1]) > abs(boom.sigma_max[1]):
        print(boom.X, boom.Y, 'z0 =     OK', 'z1 = NOT OK', boom.sigma_z)
    else:
        print(boom.X, boom.Y, 'z0 = NOT OK', 'z1 = NOT OK', boom.sigma_z)


"""
cs.plot_booms()
cs.plot_skin(True)
