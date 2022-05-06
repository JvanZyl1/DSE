import numpy as np
'''Inputs script '''
# Vehicle characteristics
l = 3               # length of the vehicle in meters [m]
D = 2               # diameter of the fuselage in meters [m]

# Propeller data
N_prop = 4     #4     # number of propellers in meters squared [m2]
R_prop = 2     #3.7       # radius of each propeller in meters [m]
B_prop = 5              # number of blades per propeller
omega_prop = 300    # rotational speed of each propeller in rpm [min-1]

# Efficiencies
eta_prop = 0.8  # efficiencies, values taken from https://arc.aiaa.org/doi/pdf/10.2514/6.2021-3169
eta_motor = 0.95
eta_power_transfer = 0.97
eta_battery = 0.95
eta_final = eta_battery * eta_prop * eta_motor * eta_power_transfer

W_PL = 250          # mass of the payload in kilograms [kg]
eta_E = 200         # energy density of the battery in [Wh/kg]

MTOW = 800        # maximum take-off weight in [kg]

PowWtRat = 7732     # power to weight ratio for the motor [W/kg]

g = 9.81            # gravitional acceleration [m/s2]

VehicleConfig = 'multirotor'
# KittyHawk - LiftCruise; Ehang 184 - Multirotor; Lilium - VectorThrust


if VehicleConfig == 'LiftCruise':     #KittyHawk
    l_t = 3.344         # length from wing c/4 to root of tail
    b = 11
    S = 10
    C_L = 1.4
    N_prop = 12
    R_prop = 0.65
    B_prop = 2
    V_cr = 180 / 3.6
    W_MTOW = 1224
    eta_E = 157
    l = 4.8
    D = 1.5
    S_nac = 3.76
    N_nac = 6
    Lambda = 0
    t_chord = 0.3
    n_ult = 2
    S_v = 1.5
    S_h = 2
    P_cruise = 200000

    b = 11              # Wing span [m]
    S = 10              # Wing surface area [m^2]
    N_prop = 12         # Number of propellers [-]
    R_prop = 0.65       # Propeller radius [m]
    B_prop = 2          # Number of blades per propeller [-]
    V_cr = 180 / 3.6    # Cruise velocity [m/s]
    MTOW = 1224         # Max take of weight [kg]
    eta_E = 157         # Energy density of battery [Wh/kg]
    l = 4.8             # Length of the vehicle [m]
    D = 1.5             # Diameter of the fuselage [m]
    S_nac = 3.76        # Nacelle ? area [m^2]
    N_nac = 6           # Number of nacelles ? [-]
    Lambda = 0          # Wing sweep [rad]
    t_chord = 0.3       # Chord length [m]
    n_ult = 2           # Ultimate load factor [-]
    S_v = 1.5           # Vertical tail surface area [m^2]
    S_h = 2             # Horizontal tail surface area [m^2]
    P_cruise = 200000   # Cruise power [W]
    # ^^^ This will be obtained from the calculations right?
elif VehicleConfig == 'VectoredThrust':
    C_L = 1.4
    S = 10
    b = 12
    V_cr = 203 / 3.6
    N_prop = 24
    D = 1.6
    l = 3.5
    R_prop = 0.20
    B_prop = 20
    RPM = 6000
    S_nac = 0.5
    N_nac = 24
    l_t = l
    energy_density = 170
    Lambda = np.arctan(15 / 182)
    t_chord = 0.14
    W_MTOW = 1000
    CL = 1.4            # Lift coefficient during ? [-]
    V_cr = 203 / 3.6    # Cruise velocity [m/s]
    N_prop = 24         # Number of propellers [-]
    D = 1.6             # Diameter of fuselage [m]
    l = 3.5             # Length of vehicle [m]
    R_prop = 0.10       # Propeller radius [m]
    B_prop = 20         # Number of blades per propeller [-]
    omega_prop = 6000   # Rotational velocity of propeller [rad/s]
    S_nac = 0.5         # Nacelle ? area [m^2]
    N_nac = 24          # Number of nacelles ? [-]
    l_t = l             # ?
    energy_density = 170 # Energy density of battery [Wh/kg]
    Lambda = np.arctan(15 / 182) # Wing sweep [rad]
    t_chord = 0.14      # Chord length [m]
    MTOW = 1000         # Max take of weight [kg]

elif VehicleConfig == 'multirotor':
    V_cr = 100 / 3.6          # Cruise velocity [m/s]
    N_prop = 4                # Number of propellers [-]
    R_prop = 0.7              # Propeller radius [m]
    B_prop = 5                # Number of blades per propeller [-]
    omega_prop = 30           # Rotational velocity of propeller [rad/s]
    MTOW = 800                # Max take of weight [kg]






# Mission profile characteristics
R = 20000           # mission range in kilometers [m]
R_div = 5000        # additional diversion range in kilometers [m]
#V_cr = 200 / 3.6   # assumed cruise speed in kilometers per hour [km/h]
V_TO = 3            # assumed take-off and descent velocity [m/s !]
h_TO = 100          # assumed vertical travel distance in [m]
rho = 1.225         # air density in [kg/m3]
n_ult = 2           # ultimate load factor
