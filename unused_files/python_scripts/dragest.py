import numpy as np
from inputs import *
from Parasitedrag_Estimation_Multirotor import parasite_drag
import matplotlib.pyplot as plt

def parasite_drag_est(R_prop_big, N_prop_big, R_prop_small, N_prop_small, V_cr):
    CD0, D_q_tot_x = parasite_drag((R_prop_big*8+R_prop_small*2)/10, N_prop_big+N_prop_small)
    D0 = 0.5 * CD0 * rho * V_cr*V_cr * D_q_tot_x
    return D0

def induced_drag_est(MTOW, A_disk):
    #T = MTOW * g / np.cos(alpha_TPP) / (N_prop_big+N_prop_small)
    #Di = T*T / (2*A_disk)

    return Di

def profile_drag_est(dtheta_deg, dr, R_prop, c, V_cr, omega_prop):
    C_d = 0.6; C_l = 1.4
    theta = 0; D = 0; L = 0
    dtheta = dtheta_deg * np.pi / 180
    for i in range(int(180/dtheta_deg)):
        theta += dtheta
        dD = 0; dL = 0
        #print("For theta = ", i*dtheta_deg)
        for r in np.arange(0, R_prop+dr, dr):
            V1 = omega_prop * r + V_cr * np.cos(theta)
            V2 = omega_prop * r + V_cr * np.cos(theta+np.pi)
            dD += 0.5 * C_d * rho * V1**2 * dr * c * 0.12 + 0.5 * C_d * rho * V2**2 * dr * c * 0.12
            dL += 0.5 * C_l * rho * V1**2 * dr * c * 0.12 + 0.5 * C_l * rho * V2**2 * dr * c * 0.12
        D += dD
        L += dL
        #print(D)
    Dp = D / (360 / (dtheta * 180 / np.pi))
    L_avg = L / (360 / (dtheta * 180 / np.pi))
    return Dp, L_avg


D0 = []; Di = []; Dp = []
V_cr_list = np.arange(50, 200, 1)
for V_cr in V_cr_list:
    D0.append(parasite_drag_est(R_prop_big, N_prop_big, R_prop_small, N_prop_small, V_cr))
    #Di.append(induced_drag_est(MTOW, A_disk))
    Dp.append(profile_drag_est(1, 0.1, R_prop_big, c_prop, V_cr, omega_prop)[0])

L_req = MTOW * 0.8 * 1.1 * g / N_prop_big + MTOW * 0.2 * 1.1 * g / N_prop_small
print(D0, Dp)

plt.figure()
plt.plot(V_cr_list, D0, color='green')
#plt.plot(V_cr_list, Di, color='blue')
plt.plot(V_cr_list, Dp, color='red')
plt.show()


