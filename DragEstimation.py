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
    '''Rotor craft angle of attack estimator'''
    #Nominal drag force on fuselage during cruise
    D = 0.5 * rho * V_cr**2* D_q_tot
    #Equilibrium AoA
    alpha = np.atan2(D,MTOW * g)
    return alpha

def Windforces(rho,Vx, Vy, Vz, V_ind, Vw_x, Vw_y, Vw_z, D_q_tot_x):
    '''Velocities and wind velocities in bodyframe.'''
    Vx_rel = Vx - Vw_x
    Vy_rel = Vy - Vw_y
    Vz_rel = Vz - Vw_z
    V_infty = np.sqrt(Vx_rel**2 +Vy_rel**2 +(Vz_rel + V_ind)**2)

    D_q_tot_y = 2.2 * D_q_tot_x # [m^2] Assumption
    D_q_tot_z = 1.5 * D_q_tot_x # [m^2] Assumption
    #The above assumptions come from http://www.israelbarrientos.org/personal/simulador_files/helimodel_gavrilet.pdf
    Fw_x = -0.5 * rho * Vx_rel * V_infty * D_q_tot_x
    Fw_y = -0.5 * rho * Vy_rel * V_infty * D_q_tot_y
    Fw_z = -0.5 *rho *(Vz_rel + V_ind) * V_infty * D_q_tot_z
    return Fw_x, Fw_y, Fw_z
