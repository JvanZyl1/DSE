'''Power Estimation Routine for a Helicopter-Config Vehicle'''
import matplotlib.pyplot as plt
import numpy as np
from inputs import *
from Parasitedrag_Estimation_Multirotor import *
from DragEstimation import DragPolar
from MassEstimation import BatteryMassFun

def Cruise_Power_estimation_rotorcraft(R_prop, N_prop, V_cr, omega_prop, rho, g, MTOW):
    '''Inputs: R_prop, N_prop, V_cr, omega_prop, rho, g, MTOW. Output: Preq_cruise.'''
    # Assumed values for power estimation

    K = 4.65                                       # 4.5 in hover to 5 at mu = .5
    sigma = 0.1                                    # solidity for the main rotor
    kappa = 1.15                                   # induced power factor
    C_d0 = 0.008                                   # profile drag coefficient of the blade
    alpha_TPP = 5                                  # angle of attack in cruise [deg]
    f = D_q_tot                                    # equivalent area estimated from reference A/C [m2]
    A_rotor = N_prop * np.pi * R_prop**2           # rotor area in [m2]                              
        
                        
    mu = (V_cr * np.cos(np.deg2rad(alpha_TPP))) / (omega_prop * R_prop) # advance ratio [~]

    # Calculate the dimensionalizing factor
    P_fact = rho * A_rotor * (R_prop*omega_prop)**3 

    # Caculate the thrust coefficient
    C_T = (MTOW * g / np.cos(np.deg2rad(alpha_TPP)) ) \
    / (rho * (R_prop * omega_prop)**2 * A_rotor)

    def CalculateP0(sigma, C_d0, K, mu, P_fact):
        C_P0 = sigma * C_d0 * (1 + (K * mu**2)) / 8
        P0 = C_P0 * P_fact
        return P0

    def CalculatePi(kappa, mu, C_T, P_fact):
        # it is assumed that mu >> lambda here
        C_Pi = kappa * C_T**2 / (2 * mu) #Induced power coefficient [-]
        Pi = C_Pi * P_fact
        return Pi

    def CalculatePp(f, A_rotor, mu, P_fact):
        C_Pp = 0.5 * mu**3 * (f/A_rotor) #Parisative power coefficient [-]
        Pp = C_Pp * P_fact
        return Pp

    P0 = CalculateP0(sigma, C_d0, K, mu, P_fact)
    Pi = CalculatePi(kappa, mu, C_T, P_fact)
    Pp = CalculatePp(f, A_rotor, mu, P_fact)
    print("Power components: ", P0, Pi, Pp)

    print('The tip speed in m/s is: ', np.round(omega_prop * R_prop * (2 * np.pi / 60),2))
    
    Preq_cruise = P0 + Pi + Pp #Total power from components [W]

    print('The power required in cruise is [kW]:', np.round((Preq_cruise/1000),2))
    return Preq_cruise
def Rotorcraft_CruiseDrag(V_cr,MTOW,Preq_cruise,S_body):
    '''Outputs order: Cruise drag, L/D and C_D'''
    D_cruise = Preq_cruise / V_cr # Total drag during cruise [N]
    L_D_cruise = (MTOW*V_cr)/Preq_cruise # L/D for cruise [-]
    return D_cruise, L_D_cruise
def PowerEstimationHover(R_prop, N_prop, MTOW):

    thrust = MTOW / N_prop

    K = 22.35   # Typical value for sealevel conditions

    P_prop = K * thrust ** 1.5 / R_prop

    P_hover = P_prop * N_prop

    print('The power required in hover is [kW]:', np.round((P_hover/1000),2))

    return P_hover


def Power_DiskActuatorTheory(MTOW, N_prop, R_prop, duct=False):
    """
    This function calculates the maximum power required (at take-off and landing)
    input: MTOW
    :return: P_max
    """
    T = MTOW * g * 1.1  # N
    if duct:
        Ti = 1.2  # Multiplication factor for ducted propeller thrust (from literature)
    else:
        Ti = 1
    A_disk = R_prop ** 2 * np.pi * N_prop  # m^2, Actuator disk area (total)
    P_max = np.sqrt((T / Ti) ** 3 / (2 * rho * A_disk))  # W
    print("Pmax = ", P_max)
    return P_max


def PowerReq(MTOW,N_prop,R_prop,V_cr):
    """Function designed for multirotors (EHang's)"""
    T = (MTOW * g) * 1.1       #10 percent safety factor
    tilt_cruise = 10       #angle of tilt during cruise in degree
    disk_area = R_prop**2 * np.pi * N_prop
    kappa = 1.2       #correction factor for extra power losses, value taken from literature
    V_perp = (V_cr * np.sin(tilt_cruise * (np.pi/180)))      #perpendicular to rotor plane free stream velocity in [m/s]
    v_i = np.sqrt((T/disk_area) * (1/(2 * rho)))           #induced velocity during hover
    P = T*V_perp + kappa * T * (-V_perp/2 + np.sqrt(V_perp**2 / 4 + T/(2 * rho * disk_area)))
    P_cruise = P / eta_final
    K_TO = 1.5     #safety factor takeoff
    T_TOL = K_TO * T
    P_TOL = (((T_TOL * V_TO)/2) * (np.sqrt(1+(2 * T_TOL)/(rho * V_TO**2 * disk_area))))/eta_final
    P_hov = P_TOL
    """From here the battery weight code is replicated with calculated values"""
    t_CR = (R + R_div) / V_cr  # Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2
    # Energy required for flight phases
    E_CR = t_CR * P_cruise
    E_TO = t_TO * P_TOL
    E_total = (E_TO + E_CR) / 3600  # total energy needed in [Wh]
    W_bat = (E_total / eta_E) / nu_discharge
    return P_cruise,P_hov,W_bat


def PowerCruiseWing(C_L, rho, V_cr, S):
    P_cruise = 0.5 * DragPolar(C_L) * rho * V_cr**3 * S / eta_final
    return P_cruise



print('propeller blade radius = ', R_prop)


print('Power required cruise = ',PowerReq(MTOW,N_prop,R_prop,V_cr)[0]/1000,' [kW]')
print('Power required takeoff = ',PowerReq(MTOW,N_prop,R_prop,V_cr)[1]/1000,' [kW]')
print('Battery weight = ',PowerReq(MTOW,N_prop,R_prop,V_cr)[2],' [kg]')


