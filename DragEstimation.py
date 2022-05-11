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
    C_D = 0.0438 + 0.0294 * (C_L**2)
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
    return 0.5 * rho * V ** 2 * parasite_drag()[1]

def FOR_AOA(V, gamma=0): #for forward flight
    return np.arcsin(drag_parasitic_fuselage(V)/ (MTOW * g) + np.sin(gamma))

def V_ind_FOR_non_dim(V, gamma=0): #for forward flight
    v_i = Symbol('v_i')
    array = solve(v_i ** 4 + (V**2 * v_i**2) + (2 * V * v_i**3 * np.sin(FOR_AOA(V, gamma))) - 1, v_i)
    return array[1]

def V_ind_FOR(V, T, gamma=0): #T is the thrust per rotor
    return V_ind_FOR_non_dim(V, gamma) * np.sqrt(T/(2 * rho * np.pi * R_prop ** 2))


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
    # Getting the induced angle of attack under the rotor. Than rotate it
    # to an airfoil perpendicular to the rotor (do: pi/2 - induced angle)
    AoA_ind = np.pi/2 - np.arctan2((V*np.sin(AoA)+Vind),V*np.cos(AoA))
    # The effective angle of attack at airfoil (so rotating with its deflection (delta))
    AoA_eff = np.pi/2 - np.arctan2((V*np.sin(AoA)+Vind),V*np.cos(AoA))- delta
    # Total velocity under rotor
    Vtot_eff = np.sqrt((V*np.sin(AoA)+Vind)**2 + (V*np.cos(AoA))**2)
    # Lift force from the deflector
    L = 0.5 * rho * Vtot_eff**2 * S_flap * C(AoA_eff, 'Cl',airfoilcsv)
    # Drag force from the deflector
    D = 0.5 * rho * Vtot_eff**2 * S_flap * C(AoA_eff, 'Cd',airfoilcsv)
    # Maybe change to 3D transformation
    # Transformation from induced aero axis system to a rotor fixed axis system.
    # x parallel to rotor and y normal down
    T = np.array([[np.cos(AoA_ind), np.sin(AoA_ind)],
                  [np.sin(AoA_ind), np.cos(AoA_ind)]])
    
    F_localaeroaxes = np.array([[L],[D]])
    F_bodyaxis = np.matmul(T,F_localaeroaxes)
    return F_bodyaxis

def AirfoilParameters(Airfoilcsv):
    '''Input csv, output dictionary with airfoil parameters'''
    #Getting airfoil data from csv
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
    #Putting values in dict
    #For AoA [rad]: Datadict['alpha']
    #For Cl [-]: Datadict['Cl']
    #For Cd [-]: Datadict['Cd']
    #For Cm [-]: Datadict['Cm']
    Datadict = {rows[10][0]: np.pi/180 * values[:,0],
                rows[10][1]: values[:,1],
                rows[10][2]: values[:,2],
                rows[10][4]: values[:,4]}
    return Datadict
#AirfoilParameters('Xfoil-NACA0012.csv')
def C(alpha,aeroparam,airfoilcsv):
    '''Input: AoA, string for aeroparam: 'Cl','Cd' or 'Cm'. Output: Aerodynamic coefficient'''
    #Finding Cl, Cd or Cm at a certain AoA.
    aerodict = AirfoilParameters(airfoilcsv)
    return np.interp(alpha, aerodict['Alpha'],aerodict[aeroparam])

def deflector_analyser():
    V=V_cr
    #Flap area. Assume that it is as wide as a rotor and assume that the chord length is 15cm.
    S_flap = 0.15 * 2 * R_prop
    #Area of 1 rotor.
    A_rot = np.pi*R_prop**2
    #Parasite drag
    D_q_tot_x = parasite_drag()[1]
    #Getting thrust and angle of attack at the specified velocity
    T = RC_AoAandThrust(V, D_q_tot_x, rho, MTOW, g)[1]
    AoA= RC_AoAandThrust(V, D_q_tot_x, rho, MTOW, g)[0]
    # Induced velocity
    Vind = V_ind(T,rho,V,AoA,A_rot)
    #Induced AoA relative to deflector
    AoA_ind = np.pi/2 - np.arctan2((V*np.sin(AoA)+Vind),V*np.cos(AoA))
    #Choosing a range of deflector deflections [rad]
    delta = np.arange(AoA_ind - 30*np.pi/180, AoA_ind + 30*np.pi/180,0.01)      
    force =[]
    for d in delta: 
        force.append(FlapForceEstimator(T, rho, V, AoA, A_rot,d, S_flap,'Xfoil-NACA0012.csv'))
    forcelst =np.array(force)
    #Plotting the force tangential to the rotor vs delta 
    plt.plot(delta,forcelst[:,0])
    plt.show()
    #Plotting the force normal to the rotor vs delta
    plt.plot(delta,forcelst[:,1])
    plt.show()
    return
