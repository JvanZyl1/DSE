import numpy as np

A = 75 # [-] Rotor aspect ratio
S_disk = 80 #[m^2] Rotor disk area
b = 2* np.sqrt(S_disk/np.pi) # [m] Span width 
c = b / A # [m] chord length
n_blades = 2 # [-] Number of blades
S_rot = n_blades* b/2 * c #[m^2] rotor planform length (assumed to be two blades)


def Est_rotor_mass(S_rot):
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    return -194.685 + 12.164*S_rot_ft2
