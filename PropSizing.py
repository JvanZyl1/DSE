import numpy as np

rho = 1.225
M = 0.9  # Estimate, efficiency of propulsion system

MTOW = 2000

S_disk = R_prop * np.pi ** 2 * N_prop  # m^2, Actuator disk area (total)
T = MTOW

hov_eff = MTOW * np.sqrt(2*rho*S_disk) / T**1.5 * Msdfa




