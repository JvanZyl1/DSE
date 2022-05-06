import numpy as np

# parameters (to be added to txt)
Cd = .2
A  = 3.5 # area in m2
m  = 827 # mass in kg
# u  = 20  # gust velocity in m/s
t  = 10.5   # time of gust in s
tau = .2 # random time delay

# functions
def gust_velocity(t):
    ''''
    where period is 10.5 seconds
    :param: t in seconds
    :return: gust velocity according to easa standard in baseline
    '''
    T = 10.5
    return 12.4 - 13*np.sin(3*np.pi*t / T)*(1 - np.cos(2*np.pi*t / T))

def aero_force(cd, area, vel, rho):
    '''
    :param cd: relevant drag coefficient
    :param area: relevant area in m2
    :param vel: gust velocity in m.s
    :param rho: density in kg/m3
    :return: force in direction of gust velocity
    '''
    return .5*rho*(vel)**2*area*cd


# reaction

dt = .01
u_side = 0
posy = 0
for i in np.arange(0,t,dt):
    u_gust = gust_velocity(t)
    u_push = u_gust - u_side
    a_gust = aero_force(Cd, A, u_push, 1.225) / m
    # NOW WE ASSUME SYMMETRICAL DRAG
    a_drag = aero_force(Cd, A, u_side, 1.225) / m
    # a_drag = 0
    a = a_gust - a_drag
    u_side += a*dt
    posy += u_side*dt

print(u_side, posy)
