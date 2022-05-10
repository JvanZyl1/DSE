'''Drag Polars as derived for specific concepts by https://www.mdpi.com/2226-4310/6/3/26 '''
import csv
from inputs import *
from Parasitedrag_Estimation_Multirotor import *
import scipy.optimize as sc
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt

def DragPolar(C_L):
    '''Lift drag estimations for lift&cruise and VectorThrust.'''
    if VehicleConfig == 'LiftCruise':
        C_D = 0.0438 + 0.0294 * (C_L**2)
    elif VehicleConfig == 'VectorThrust':
        C_D = 0.0163 + 0.058 * (C_L**2)
    return C_D

def RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g):
    '''Rotor craft angle of attack estimator'''
    #Nominal drag force on fuselage during cruise
    D = 0.5 * rho * V_cr**2* D_q_tot_x
    #Equilibrium AoA
    alpha = np.arctan2(D,MTOW * g)
    Treq = np.sqrt(MTOW**2 + D**2)
    return alpha, Treq

def V_ind(T,rho,V,AoA,A_rot):
    '''Thrust and A_rot for 1 rotor.'''
    def thrust_eq(V_ind,T,rho,V,AoA,A_rot):
        f = T - 2*rho*A_rot*V_ind*np.sqrt(V**2 + 2*V*V_ind*np.sin(AoA) + V_ind**2)
        return f
    V_ind_found = sc.newton(thrust_eq, V, args = (T,rho,V,AoA,A_rot))
    return V_ind_found

def drag_parasitic_fuselage(V): #for forward flight
    return 0.5 * rho * V ** 2 * D_q_tot_x

def FOR_AOA(V, gamma=0): #for forward flight
    return np.arcsin(drag_parasitic_fuselage(V)/ (MTOW * g) + np.sin(gamma))

def V_ind_FOR_non_dim(V, gamma=0): #for forward flight
    v_i = Symbol('v_i')
    array = solve(v_i ** 4 + (V**2 * v_i**2) + (2 * V * v_i**3 * np.sin(FOR_AOA(V, gamma))) - 1, v_i)
    return array[1]

def V_ind_FOR(V, T, R, gamma=0):
    return V_ind_FOR_non_dim(V) * np.sqrt(T/(2 * rho * np.pi * R ** 2))


def Windforces_RC(rho,Vx, Vy, Vz, V_ind, Vw_x, Vw_y, Vw_z):
    '''Velocities and wind velocities in bodyframe. It outputs the wind forces in three dimensions (bodyframe)'''
    CY = 0.6 # Lateral force coefficient
    CX = parasite_drag()[0]  # Reference area is the fuselage wetted area
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
    CY_fus = 0.6
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
def FlapForceEstimator(T, rho, V, AoA, A_rot,delta, S_flap,airfoilcsv):
    A_rot = np.pi * R_prop**2 #[m^2]
    Vind = V_ind(T,rho,V,AoA,A_rot)
    AoA_ind = np.pi/2 - np.arctan2((V*np.sin(AoA)+Vind),V*np.cos(AoA))

    AoA_eff = np.pi/2 - np.arctan2((V*np.sin(AoA)+Vind),V*np.cos(AoA))- delta
    Vtot_eff = np.sqrt((V*np.sin(AoA)+Vind)**2 + (V*np.cos(AoA))**2)
    L = 0.5 * rho * Vtot_eff**2 * S_flap * C(AoA_eff, 'Cl',airfoilcsv)
    D = 0.5 * rho * Vtot_eff**2 * S_flap * C(AoA_eff, 'Cd',airfoilcsv)
    # Maybe change to 3D transformation
    T = np.array([[np.cos(AoA_ind), np.sin(AoA_ind)],
                  [np.sin(AoA_ind), np.cos(AoA_ind)]])
    F_localaeroaxes = np.array([[L],[D]])
    F_bodyaxis = np.matmul(T,F_localaeroaxes)
    return F_bodyaxis

def AirfoilParameters(Airfoilcsv):
    '''Input csv, output dictionary with airfoil parameters'''
    data = open(Airfoilcsv,'r')
    dat = csv.reader(data)
    rows =[]
    for row in dat:
        rows.append(row)
    values = rows[11:]   
    for line in values:
        for el in line:
            line[line.index(el)] = float(el)
        values[values.index(line)] = line
    values = np.array(values)
    Datadict = {rows[10][0]: np.pi/180 * values[:,0],
                rows[10][1]: values[:,1],
                rows[10][2]: values[:,2],
                rows[10][4]: values[:,4]}
    return Datadict
#AirfoilParameters('Xfoil-NACA0012.csv')
def C(alpha,aeroparam,airfoilcsv):
    '''Input: AoA, string for aeroparam: 'Cl','Cd' or 'Cm'. Output: Aerodynamic coefficient'''
    aerodict = AirfoilParameters(airfoilcsv)
    return np.interp(alpha, aerodict['Alpha'],aerodict[aeroparam])

def deflector_analyser():
    V_cr = 0
    S_flap = 0.15 * 2 * R_prop
    delta = np.arange(-15,-15,0.01)
    A_rot = np.pi*R_prop**2
    D_q_tot_x = parasite_drag()[1]
    delta = np.arange(-15*np.pi/180,15*np.pi/180,0.01)
    T = RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g)[1]
    AoA= RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g)[0]
    A_rot = np.pi*R_prop**2
    Vind = V_ind(T,rho,V_cr,AoA,A_rot)
    AoA_ind = np.pi/2 - np.arctan2((V_cr*np.sin(AoA)+Vind),V_cr*np.cos(AoA))
    delta = np.arange(AoA_ind - 30*np.pi/180, AoA_ind + 30*np.pi/180,0.01)
    print(FlapForceEstimator(T, rho, V_cr, AoA, A_rot,AoA_ind, S_flap,'Xfoil-NACA0012.csv'))
    
    
    force =[]
    for d in delta: 
        force.append(FlapForceEstimator(T, rho, V_cr, AoA, A_rot,d, S_flap,'Xfoil-NACA0012.csv'))
    forcelst =np.array(force)
    plt.plot(delta,forcelst[:,0])
    plt.show()
    plt.plot(delta,forcelst[:,1])
    plt.show()
    return
