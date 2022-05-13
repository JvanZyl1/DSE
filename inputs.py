import numpy as np
'''Inputs script '''

# Efficiencies
eta_prop = 0.8  # efficiencies, values taken from https://arc.aiaa.org/doi/pdf/10.2514/6.2021-3169
eta_motor = 0.95
eta_power_transfer = 0.97
eta_battery = 0.95
eta_final = eta_battery * eta_prop * eta_motor * eta_power_transfer
eta_E = 170         # energy density of the battery in [Wh/kg]
nu_discharge = 0.8  # discharge ratio of the battery for optimal lifetime
PowWtRat = 7732     # power to weight ratio for the motor [W/kg]
g = 9.81            # gravitional acceleration [m/s2]

# KittyHawk - LiftCruise;
# joby s4 - VectoredThrust;
# Ehang 184 - Multirotor;
VehicleConfig = 'Multirotor'
if VehicleConfig == 'LiftCruise':     #KittyHawk
    Wing=True
    l_t = 3.344         # length from wing c/4 to root of tail
    C_L = 0.8           # Lift coefficient in cruise
    b = 11              # Wing span [m]
    S = 10              # Wing surface area [m^2]
    N_prop = 12         # Number of propellers [-]
    R_prop = 0.65       # Propeller radius [m]
    B_prop = 2          # Number of blades per propeller [-]
    V_cr = 180 / 3.6    # Cruise velocity [m/s]
    MTOW = 1224         # Max take of weight [kg]
    l = 4.8             # Length of the vehicle [m]
    D = 1.5             # Diameter of the fuselage [m]
    S_nac = 3.76        # Nacelle ? area [m^2]
    N_nac = 6           # Number of nacelles ? [-]
    omega_prop = 3500 * 2 * np.pi / 60    # Rotational velocity of propeller [rad/s]
    Lambda = 0          # Wing sweep [rad]
    t_chord = 0.3       # Thickness of the chord at the root
    n_ult = 2           # Ultimate load factor [-]
    S_v = 1.5           # Vertical tail surface area [m^2]
    S_h = 2             # Horizontal tail surface area [m^2]
    t_rh = 0.2
    t_rv = 0.15
    Lambda_v = 30
    A_v = 3
    A_h = 3
    W_PL = 250              # mass of the payload in kilograms [kg]
    R_pyl = 0.05            # Pylon radius (assumed circular) [m]
    l_pyl = 0.2             # Pylon length [m]
    CY = 0.6                # Assumed fuselage side drag coefficient
    S_side = np.pi * l*D/4  # Side fuselage area (ellipse) [m^2]


elif VehicleConfig == 'VectoredThrust':
    Wing = True
    C_L = 0.8           # Lift coefficient in cruise
    S = 10
    b = 10.7
    V_cr = 322 / 3.6    # Cruise velocity [m/s]
    N_prop = 6         # Number of propellers [-]
    D = 2             # Diameter of fuselage [m]
    l = 7.3            # Length of vehicle [m]
    R_prop = 1.5       # Propeller radius [m]
    B_prop = 5         # Number of blades per propeller [-]
    omega_prop = 300   # Rotational velocity of propeller [rad/s]
    S_nac = 0.5         # Nacelle ? area [m^2]
    N_nac = 6          # Number of nacelles ? [-]
    l_t = 3.7             # length from wing c/4 to root of tail [m]
    Lambda = -np.arctan(56/262)          # Wing sweep [rad]
    t_chord = 0.14      # Thickness of the chord at the root
    MTOW = 2415         # Max take of weight [kg]
    W_PL = 600          # mass of the payload in kilograms [kg]
    S_h = 2
    S_v = 1.5
    t_rh = 0.2
    t_rv = 0.15
    Lambda_v = 30
    A_v = 3
    A_h = 3
    R_pyl = 0.05  # Pylon radius (assumed circular) [m]
    l_pyl = 0.2   # Pylon length [m]
    CY = 0.6      # Assumed fuselage side drag coefficient
    S_side = np.pi * l*D/4  # Side fuselage area (ellipse) [m^2]

elif VehicleConfig == 'Multirotor':
    Wing = False
    l = 2.1
    D = 1.0
    V_cr = 100 / 3.6    # Cruise velocity [m/s]
    N_prop = 8          # Number of propellers [-]
    R_prop = 0.8        # Propeller radius [m]
    B_prop = 2          # Number of blades per propeller [-]
    MTOW = 350          # Max take of weight [kg]
    S_body = np.pi ** 2 * l * D / 4  # Assume fuselage to be an ellipse of revolution and calculate its wetted area
    l_t = l
    S_nac = 0
    N_nac = 0
    W_PL = 120          # mass of the payload in kilograms [kg]
    R_pyl = 0.05  # Pylon radius (assumed circular) [m]
    l_pyl = 0.2   # Pylon length [m]
    CY = 0.6      # Assumed fuselage side drag coefficient
    S_side = np.pi * l*D/4  # Side fuselage area (ellipse) [m^2]
    # Parameters for in-plane control propellers
    R_cont = 0.2
    N_cont = 3
    B_cont = 5

elif VehicleConfig=="DesignConcept":
    Wing = False
    l = 2.1
    D = 1.0
    V_cr = 100 / 3.6  # Cruise velocity [m/s]
    N_prop = 12  # Number of propellers [-]
    R_prop = 0.93  # Propeller radius [m]
    B_prop = 2  # Number of blades per propeller [-]
    MTOW = 650  # Max take of weight [kg]
    S_body = np.pi ** 2 * l * D / 4  # Assume fuselage to be an ellipse of revolution and calculate its wetted area
    l_t = l
    S_nac = 0
    N_nac = 0
    W_PL = 250  # mass of the payload in kilograms [kg]
    R_pyl = 0.05  # Pylon radius (assumed circular) [m]
    l_pyl = 0.2  # Pylon length [m]
    CY = 0.6  # Assumed fuselage side drag coefficient
    S_side = np.pi * l * D / 4  # Side fuselage area (ellipse) [m^2]
    # Parameters for in-plane control propellers
    R_cont = 0.2
    N_cont = 3
    B_cont = 5

# Cost inputs
yop = 2025              # Year of the start of production is expected
# CPI_now = 1.27          # 1 dollar in 2012 (date of literature) is worth as much as 1.27 now, found in https://www.bls.gov/data/inflation_calculator.htm
ex_rate = 0.90          # Exchange rate dollar -> euro = 0.92
# cost_per_motor = 5500   # €, estimate on price of an Emrax motor (used for other power estimations as well)
N_ps = 750              # Estimation of product series over 5 years
N_psm = N_ps/(12*5)              # Estimation of product series over 1 month
N_proto = 5             # Estimation of number of prototypes created for testing purposes

# Motor inputs
torque = 90  # Nm, for EMRAX 268 motor, https://emrax.com/wp-content/uploads/2017/10/user_manual_for_emrax_motors.pdf
av_power = 20000
max_power = 60000  # W
omega_prop = 3500 * 2 * np.pi / 60  # Rotational velocity of propeller [rad/s]
omega_max = 6500 * 2 * np.pi / 60

# Mission profile characteristics
R = 20000           # mission range in kilometers [m]
R_div = 5000        # additional diversion range in kilometers [m]
V_TO = 3            # assumed take-off and descent velocity [m/s !]
h_TO = 100          # assumed vertical travel distance in [m]
rho = 1.225         # air density in [kg/m3]
n_ult = 2           # ultimate load factor

# Wind speed
V_wind_avg = 20.7   #[m/s], average wind speed at 8 beaufort