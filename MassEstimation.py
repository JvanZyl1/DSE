import numpy as np


def Est_rotor_mass(S_rot):
    '''Input rotor planform area'''
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    M_rot_sys = (-194.685 + 12.164*S_rot_ft2)*0.4536 #Helicopter rotor mass estimation
    return M_rot_sys
def Est_MEW
