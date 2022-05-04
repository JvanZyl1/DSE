import numpy as np
'''Inputs script '''
# Vehicle characteristics
l = 3               # length of the vehicle in meters [m]
D = 2               # diameter of the fuselage in meters [m]
S_body = np.pi**2*l*D/4 # Surface area of ellipse rotated around its longitudinal axis
N_prop = 4     #4     # number of propellers in meters squared [m2]
R_prop = 5     #3.7       # radius of each propeller in meters [m]
C_prop = 0.5        # Rotor blade chord length [m]
omega_prop = 300    # rotational speed of each propeller in rpm [min-1]
W_PL = 250          # mass of the payload in kilograms [kg]
eta_E = 200         # energy density of the battery in [Wh/kg]

W_MTOW = 800        # maximum take-off weight in [kg]

PowWtRat = 7732     # power to weight ratio for the motor [W/kg]

g = 9.81            # gravitional acceleration [m/s2]
S_rot_pl = N_prop * R_prop * C_prop # Rotor planform area [m^2]

VehicleConfig = 'LiftCruise'
# KittyHawk - LiftCruise; Ehang 184 - Multirotor; Lilium - VectorThrust


if VehicleConfig == 'LiftCruise':
    l_t = 3.344         # length from wing c/4 to root of tail

# Mission profile characteristics
R = 20              # mission range in kilometers [km]
R_div = 5           # additional diversion range in kilometers [km]
V_cr = 200          # assumed cruise speed in kilometers per hour [km/h]
V_TO = 3            # assumed take-off and descent velocity [m/s !]
h_TO = 100          # assumed vertical travel distance in [m]
rho = 1.225         # air density in [kg/m3]

n_ult = 2           # ultimate load factor