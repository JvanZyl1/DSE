import numpy as np
from inputs import *

C_d = 0.6
C_l = 1.4
theta = 0
D = 0
L = 0
dtheta = 1 * np.pi / 180
dr = 0.1
for i in range(360):
    theta += dtheta
    r = 0
    dD = 0
    dL = 0
    print("For theta = ", i)
    for r in np.arange(0, R_prop+dr, dr):
        V = omega_prop * r + V_cr * np.cos(theta)
        print("V = ", V)

        dD += 0.5 * C_d * rho * V**2 * dr * 0.12

        dL += 0.5 * C_l * rho * V**2 * dr * 0.12
    D += dD
    L += dL

D_avg = B_prop * D / (360/(dtheta*180/np.pi))
L_avg = B_prop * L / (360/(dtheta*180/np.pi))
L_req = MTOW * 1.1 * g / 8
print(D_avg, L_avg, L_req)
