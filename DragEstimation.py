'''Drag Polars as derived for specific concepts by https://www.mdpi.com/2226-4310/6/3/26 '''

from inputs import *
from Parasitedrag_Estimation_Multirotor import *
import scipy.optimize as sc

def DragPolar(C_L):
    '''Lift drag estimations for lift&cruise and VectorThrust.'''
    if VehicleConfig == 'LiftCruise':
        C_D = 0.0438 + 0.0294 * (C_L**2)
    elif VehicleConfig == 'VectorThrust':
        C_D = 0.0163 + 0.058 * (C_L**2)
    return C_D
def RC_AoA(V_cr, D_q_tot_x, rho, MTOW, g):
    '''Rotor craft angle of attack estimator'''
    #Nominal drag force on fuselage during cruise
    D = 0.5 * rho * V_cr**2* D_q_tot_x
    #Equilibrium AoA
    alpha = np.arctan2(D,MTOW * g)
    return alpha
def V_ind(T,rho,V,AoA,A_rot):
    
    def thrust_eq(V_ind,T,rho,V,AoA,A_rot):
        f = T - 2*rho*A_rot*V_ind*np.sqrt(V**2 + 2*V*V_ind*np.sin(AoA) + V_ind**2)
        return f
    V_ind_found = sc.newton(thrust_eq, V, args = (T,rho,V,AoA,A_rot))
    return V_ind_found
def Windforces_RC(rho,Vx, Vy, Vz, V_ind, Vw_x, Vw_y, Vw_z):
    '''Velocities and wind velocities in bodyframe. It outputs the wind forces in three dimensions (bodyframe)'''
    CY = 0.5 # The drag coefficient is assumed to be of a sphere for the sides
    CX = CD0 # Reference area is the fuselage wetted area
    Vx_rel = Vx - Vw_x
    Vy_rel = Vy - Vw_y
    Vz_rel = Vz - Vw_z
    #http://www.israelbarrientos.org/personal/simulador_files/helimodel_gavrilet.pdf
    V_infty = np.sqrt(Vx_rel**2 +Vy_rel**2 +(Vz_rel + V_ind)**2)
    #Assume the body again to be a revoluted ellipse.
    S_fus = np.pi**2 * l * D/4 #Fuselage wetted area
    S_side = np.pi * l*D/4 # Side fuselage area (ellipse)
    Fw_x = -0.5 * rho * Vx_rel * V_infty * S_fus *CX
    Fw_y = -0.5 * rho * Vy_rel * V_infty * S_side * CY
    #Fw_z = -0.5 *rho *(Vz_rel + V_ind) * V_infty * S_side * CZ
    print("order: Fw_x, Fw_y")
    return Fw_x, Fw_y
def Windforces_AC(rho,Vx, Vy, Vz, V_ind, Vw_x, Vw_y, Vw_z, CL):
    '''Velocities and wind velocities in bodyframe. It outputs the wind forces in three dimensions (bodyframe)'''
    S_fus = np.pi**2 * l * D/4 #Fuselage wetted area
    CX = DragPolar(CL)
    CY_fus = 0.5
    CD_vertplate = 1.28
    CD_horplate = 0.01 # For wing estimate drag from flat plate.
    S_side = np.pi * l*D/4 # Side fuselage area (ellipse)
    if VehicleConfig == 'LiftCruise':
        CY = 1/S_side*(S_fus * CY_fus + (S + S_h) * CD_horplate + S_v * CD_vertplate)
    elif VehicleConfig == 'VectoredThrust':
        CY = 1/S_side *(S_fus * CY_fus + S * CD_horplate)
    Vx_rel = Vx - Vw_x
    Vy_rel = Vy - Vw_y
    Vz_rel = Vz - Vw_z
    V_infty = np.sqrt(Vx_rel**2 +Vy_rel**2 +(Vz_rel + V_ind)**2)
    Fw_x = -0.5 * rho * Vx_rel * V_infty * S_fus * CX
    Fw_y = -0.5 * rho * Vy_rel * V_infty * S_side * CY
    print("order: Fw_x, Fw_y")
    return Fw_x, Fw_y
