'''Power Estimation Routine for a Helicopter-Config Vehicle'''
import matplotlib.pyplot as plt
import numpy as np
from inputs import *

def PowerEstimationFun(R_prop, N_prop, V_cr, omega_prop, rho, g, M_MTOW):
    # Assumed values for power estimation

    K = 4.5             #
    sigma = 0.1         # solidity for the main rotor
    kappa = 1.15        # induced power factor
    C_d0 = 0.008        # profile drag coefficient of the blade
    alpha_TPP = 5       # angle of attack in cruise [deg]
    f = 0.5             # equivalent flat plate area of the fulselage [m2]

    A_rotor = N_prop * np.pi * R_prop**2     # rotor area in [m2]
    mu = (V_cr * 1000 / (60*60)) / omega_prop * R_prop * (2 * np.pi / 60)
                        # advance ratio [~]

    # Calculate the dimensionalizing factor
    P_fact = rho * A_rotor * R_prop**3 * (omega_prop
    * (2 * np.pi / 60))**3

    # Caculate the thrust coefficient
    C_T = (M_MTOW * g / np.cos(np.deg2rad(alpha_TPP)) ) \
    / ((rho * R_prop**2 * (omega_prop * (2 * np.pi / 60))**2) * rho * A_rotor)

    def CalculateP0(sigma, C_d0, K, mu, P_fact):
        C_P0 = sigma * C_d0 * (1 + (K * mu**2)) / 8
        P0 = C_P0 * P_fact
        return P0

    def CalculatePi(kappa, mu, C_T, P_fact):
        C_Pi = kappa * C_T**2 / (2 * mu)
        Pi = C_Pi * P_fact
        return Pi

    def CalculatePp(f, A_rotor, mu, P_fact):
        C_Pp = 0.5 * mu**3 * (f/A_rotor)
        Pp = C_Pp * P_fact
        return Pp

    P0 = CalculateP0(sigma, C_d0, K, mu, P_fact)
    Pi = CalculatePi(kappa, mu, C_T, P_fact)
    Pp = CalculatePp(f, A_rotor, mu, P_fact)
    print("Power components: ", P0, Pi, Pp)

    print('The tip speed in m/s is: ', np.round(omega_prop * R_prop * (2 * np.pi / 60),2))
    P_cruise = P0 + Pi + Pp
    print('The power required in cruise is [kW]:', np.round((P_cruise/1000),2))
    return P_cruise

def PowerEstimationHover(R_prop, N_prop, M_MTOW):

    thrust = M_MTOW / N_prop

    K = 22.35   # Typical value for sealevel conditions

    P_prop = K * thrust ** 1.5 / R_prop

    P_hover = P_prop * N_prop

    print('The power required in hover is [kW]:', np.round((P_hover/1000),2))

    return P_hover

def MaxPowerEstimation(MTOW, N_prop, R_prop, duct=False):
    """
    This function calculates the maximum power required (at take-off and landing)
    input: MTOW
    :return:
    """
    T = MTOW   # N

    if duct:
        Ti = 1.2  # Multiplication factor for ducted propeller thrust (from literature)
    else:
        Ti = 1

    disk_area = R_prop * np.pi ** 2 * N_prop  # m^2, Actuator disk area (total)

    P_max = np.sqrt((T / Ti) ** 3 / (2 * rho * disk_area))  # W

    return P_max

