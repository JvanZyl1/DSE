import numpy as np
'''Inputs script '''
# Vehicle characteristics
#l = 3               # length of the vehicle in meters [m]
#D = 2               # diameter of the fuselage in meters [m]
# Propeller data
#N_prop = 4     #4     # number of propellers in meters squared [m2]
#R_prop = 2     #3.7       # radius of each propeller in meters [m]
#B_prop = 5              # number of blades per propeller
#omega_prop = 300    # rotational speed of each propeller in rpm [min-1]

# Efficiencies
eta_prop = 0.8  # efficiencies, values taken from https://arc.aiaa.org/doi/pdf/10.2514/6.2021-3169
eta_motor = 0.95
eta_power_transfer = 0.97
eta_battery = 0.95
eta_final = eta_battery * eta_prop * eta_motor * eta_power_transfer
eta_E = 200         # energy density of the battery in [Wh/kg]
nu_discharge = 0.8  # discharge ratio of the battery for optimal lifetime

PowWtRat = 7732     # power to weight ratio for the motor [W/kg]

g = 9.81            # gravitional acceleration [m/s2]

# KittyHawk - LiftCruise;
# Lilium Jet - VectorThrust;
# Ehang 184 - Multirotor
VehicleConfig = 'LiftCruise'
if VehicleConfig == 'LiftCruise':     #KittyHawk
    Wing=True
    l_t = 3.344         # length from wing c/4 to root of tail [m]
    C_L = 1.2           # Lift coefficient in cruise
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
    t_chord = 0.3       # Thickness of the chord at the root
    n_ult = 2           # Ultimate load factor [-]
    S_v = 1.5           # Vertical tail surface area [m^2]
    S_h = 2             # Horizontal tail surface area [m^2]
    # P_cruise = 200000   # Cruise power [W]
    # ^^^ This will be obtained from the calculations right? Yes
    # Planform Characteristics
    t_rh = 0.2
    t_rv = 0.15
    Lambda_v = 30
    A_v = 3
    A_h = 3
    W_PL = 250          # mass of the payload in kilograms [kg]


elif VehicleConfig == 'VectoredThrust':
    Wing = True
    C_L = 0.52           # Lift coefficient in cruise
    S = 10
    b = 12
    V_cr = 203 / 3.6    # Cruise velocity [m/s]
    N_prop = 24         # Number of propellers [-]
    D = 1.6             # Diameter of fuselage [m]
    l = 3.5             # Length of vehicle [m]
    R_prop = 0.10       # Propeller radius [m]
    B_prop = 20         # Number of blades per propeller [-]
    omega_prop = 6000   # Rotational velocity of propeller [rad/s]
    S_nac = 0.5         # Nacelle ? area [m^2]
    N_nac = 24          # Number of nacelles ? [-]
    l_t = l             # length from wing c/4 to root of tail [m]
    Lambda = 0          # Wing sweep [rad]
    t_chord = 0.14      # Thickness of the chord at the root
    MTOW = 1000         # Max take of weight [kg]
    W_PL = 250          # mass of the payload in kilograms [kg]


elif VehicleConfig == 'Multirotor':
    Wing = False
    l = 2.1
    D = 1.0
    V_cr = 100 / 3.6    # Cruise velocity [m/s]
    N_prop = 12          # Number of propellers [-]
    R_prop = 0.7        # Propeller radius [m]
    B_prop = 2          # Number of blades per propeller [-]
    omega_prop = 300    # Rotational velocity of propeller [rad/s]
    MTOW = 350          # Max take of weight [kg]
    S_body = np.pi ** 2 * l * D / 4  # Assume fuselage to be an ellipse of revolution and calculate its wetted area
    l_t = l
    S_nac = 0
    N_nac = 0
    W_PL = 120          # mass of the payload in kilograms [kg]

# Cost inputs
yop = 2025              # Year of the start of production is expected
# CPI_now = 1.27          # 1 dollar in 2012 (date of literature) is worth as much as 1.27 now, found in https://www.bls.gov/data/inflation_calculator.htm
ex_rate = 0.90          # Exchange rate dollar -> euro = 0.92
# cost_per_motor = 5500   # €, estimate on price of an Emrax motor (used for other power estimations as well)
N_ps = 500              # Estimation of product series over 5 years
N_psm = 20              # Estimation of product series over 1 month
N_proto = 5             # Estimation of number of prototypes created for testing purposes


# Mission profile characteristics
R = 20000           # mission range in kilometers [m]
R_div = 5000        # additional diversion range in kilometers [m]
V_TO = 3            # assumed take-off and descent velocity [m/s !]
h_TO = 100          # assumed vertical travel distance in [m]
rho = 1.225         # air density in [kg/m3]
n_ult = 2           # ultimate load factor
