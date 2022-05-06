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
CD_fus = 0.0045 #use the wetted area as reference area
CD_rot = 0.0045 #use rotor disk area
CD_pyl = 0.025  #use pylon wet area
D_q_landinggear = 0.2*0.3048**2 #Landing gear CDA [m^2]
D_q_tot_ref = 3.43*0.3048**2 #Total CDA of the reference quadcopter from the paper[m^2] 
D_q_fus_ref = 0.58 * 0.3048**2 #Fuselage CDA of the reference quadcopter [m^2]
D_q_rot_ref = 2.65 * 0.3048**2 #Rotor CDA of the reference quadcopter [m^2]
S_disk_ref = 4*np.pi * (6.31 *0.3048)**2 #Reference rotor disk area [m^2]
D_q_rothub_ref = S_disk_ref * CD_rot # Reference rotor disk area [m^2]
D_q_pylons_ref = D_q_rot_ref - D_q_rothub_ref # Estimating rotor pylon drag [m^2]
S_pylon = D_q_pylons_ref/(0.025*4) # Estimated pylon wet area [m^2]

#Own design estimated from above parameters
S_fus = np.pi**2*l*D/4 #Fuselage wetted area [m^2]
S_disk = np.pi*R_prop**2*N_prop #Rotor disk area [m^2]
# Parasite CDA
D_q_tot = (CD_fus*S_fus + CD_rot*S_disk + 4*CD_pyl*S_pylon + D_q_landinggear)
# Assume that the reference area is the fuselage area
CD0 = D_q_tot/S_fus #parasitic drag coefficient
print('CD0:', CD0)
