from math import log10

# Vehicle parameters
r_fus  = 1.5 # [m] radius of fuselage
r_prop = 1   # [m] radius of propellers
nr_emg = 4   # [m] number of engines
w = 5        # [m] width of the vehicle

# flight conditions
h = 700    # [m] altitude
V = 100/3.6 # [m/s] forward velocity

# ISA calculator
def isa(alt):
    '''Can be used up to 11,000 m altitude.
    returns p, rho, T'''
    rho0 = 1.225  # [kg/m3]
    T0   = 288.15 # [K]
    p0   = 101325 # [Pa]
    a    = 0.0065    # [K/m]
    R    = 287
    g0   = 9.8665


    T = T0 - a*alt
    p = p0*(T/T0)**(g0/(a*R))
    rho = p/(R*T)
    # rho = rho0*(T/T0)**(-(g0/(a*R)+1)
    return p, rho, T
# Reynolds number
def re(V,alt, l):
    '''Returns Reynolds number for certain characteristic length.'''
    mu = 1.4207e-5
    rho = isa(alt)[1]
    return rho*V*l/mu
# drag estimation of the fuselage, estimating as sphere
l = 2*r_fus
rho = isa(h)[1]
print(isa(h))
mu = 1.7893e-5
Re = rho*V*l/mu
print(log10(Re))
#For a quadrotor. Found at https://ntrs.nasa.gov/api/citations/20180003381/downloads/20180003381.pdf
CD_fus = 0.0045 #use the wetted area as reference area
CD_rothub = 0.0045 #use the rotor disk area as reference area
CD_rotpylon = 0.025 #use wetted area
D_q_landinggear = 0.2
D_q_tot = 3.43*0.3048**2 #[m^2] Total CDA of a quadcopter
