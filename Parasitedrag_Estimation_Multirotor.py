from math import log10
from inputs import *
import numpy as np
# Vehicle parameters
##r_fus  = 1.5 # [m] radius of fuselage
##r_prop = 1   # [m] radius of propellers
##nr_emg = 4   # [m] number of engines
##w = 5        # [m] width of the vehicle
##
### flight conditions
##h = 700    # [m] altitude
##V = 100/3.6 # [m/s] forward velocity
##
### ISA calculator
##def isa(alt):
##    '''Can be used up to 11,000 m altitude.
##    returns p, rho, T'''
##    rho0 = 1.225  # [kg/m3]
##    T0   = 288.15 # [K]
##    p0   = 101325 # [Pa]
##    a    = 0.0065    # [K/m]
##    R    = 287
##    g0   = 9.8665
##
##
##    T = T0 - a*alt
##    p = p0*(T/T0)**(g0/(a*R))
##    rho = p/(R*T)
##    # rho = rho0*(T/T0)**(-(g0/(a*R)+1)
##    return p, rho, T
### Reynolds number
##def re(V,alt, l):
##    '''Returns Reynolds number for certain characteristic length.'''
##    mu = 1.4207e-5
##    rho = isa(alt)[1]
##    return rho*V*l/mu
### drag estimation of the fuselage, estimating as sphere
###l = 2*r_fus
##rho = isa(h)[1]
##print(isa(h))
##mu = 1.7893e-5
##Re = rho*V*l/mu
##print(log10(Re))

#For a quadrotor. Found at https://ntrs.nasa.gov/api/citations/20180003381/downloads/20180003381.pdf
CD_fus = 0.4 #use the fuselage crossectional area. CD is assumed from an ellipse.
CD_rot = 0.0045 #use rotor disk area
CD_pyl = 0.025  #use pylon wet area
D_q_landinggear = 0.2*0.3048**2 #Landing gear CDA [m^2]

S_pylon = l_pyl * 2*np.pi *R_pyl*N_prop # Estimated pylon wet area [m^2]

#Own design estimated from above parameters
S_fus = np.pi*D**2/4 #Fuselage cross-sectional area [m^2]
S_disk = np.pi*R_prop**2*N_prop #Rotor disk area [m^2]
# Parasite CDA
D_q_tot_x = (CD_fus*S_fus + CD_rot*S_disk + N_prop*CD_pyl*S_pylon + D_q_landinggear)
# Assume that the reference area is the fuselage crosssectional area
CD0 = D_q_tot_x/S_fus #parasitic drag coefficient
print('CD0:', CD0)

