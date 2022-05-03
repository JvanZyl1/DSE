import numpy as np


def Est_rotor_mass(S_rot):
    '''Input rotor planform area'''
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    M_rot_sys = (-194.685 + 12.164*S_rot_ft2)*0.4536 # [kg] Helicopter rotor mass estimation
    return M_rot_sys
def Body(S_body):
    '''Input body surface area'''
    S_body_ft2 = S_body/(0.3048**2) #[ft^2]
    M_body = (-269.023 + 2.356 * S_body_ft2)*0.4536 # [kg] Estimation relation
    return M_body
