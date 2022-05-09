'''Drag Polars as derived for specific concepts by https://www.mdpi.com/2226-4310/6/3/26 '''

from inputs import *
from Parasitedrag_Estimation_Multirotor import *

def DragPolar(C_L):
    '''Lift drag estimations for lift&cruise and VectorThrust.'''
    if VehicleConfig == 'LiftCruise':
        C_D = 0.0438 + 0.0294 * (C_L**2)
    elif VehicleConfig == 'VectorThrust':
        C_D = 0.0163 + 0.058 * (C_L**2)
    return C_D
def RC_AoA(V_cr, D_q_tot, rho, MTOW, g):
    #Nominal drag force on fuselage during cruise
    D = 0.5 * rho * V_cr**2* D_q_tot
    #Equilibrium AoA
    alpha = np.atan2(D,MTOW * g)
    return alpha
