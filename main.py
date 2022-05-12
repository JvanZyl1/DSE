'''Conceptual Design of the Urban Air Vehicle'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from inputs import *
from PowerEstimation import *
from MassEstimation import *
from CostEstimation import *

# Weight Estimation routine for KittyHawk

n_iter = 20
for i in range(n_iter):

    # Power estimation
    P_TOL = PowerReq(MTOW, N_prop, R_prop, V_cr)[1]
    if Wing:
        P_cruise = PowerCruiseWing(C_L, rho, V_cr, S)
        P_TOL = PowerReq(MTOW, N_prop, R_prop, V_cr)[1]
    else:
        P_cruise = PowerReq(MTOW, N_prop, R_prop, V_cr)[0]
        P_cruise, P_TOL = PowerReq(MTOW, N_prop, R_prop, V_cr)
    print("Hover power: ", P_TOL, '\n',
          "Cruise power: ", P_cruise)

    # Weight estimation
    BatWt, BatWts, E_total = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, nu_discharge)
    PropWt, PropWts = PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL)
    FuseWt, FuseWts = FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac)
    if Wing:
        WingWt, WingWts = WingGroupMassFun(MTOW, W_PL, b, S, n_ult)
        TailWt, TailWts = TailplaneGroupFun(MTOW, S_h, t_rh, t_rv, Lambda_v, A_v, A_h)
        Weights = np.vstack((BatWts,PropWts,FuseWts, WingWts, TailWts))
        MTOW = np.sum([PropWt, WingWt, FuseWt, TailWt, BatWt, W_PL])
    else:
        Weights = np.vstack((BatWts,PropWts,FuseWts))
        MTOW = np.sum([PropWt, FuseWt, BatWt, W_PL])
    # print(Weights)
    print("MTOW: ", MTOW)

    # Cost estimation
    W_struct = MTOW - (BatWt + PropWt + W_PL)
    C_unit, C_overhead, C_list = total_costs(W_struct, E_total, P_TOL, R_prop)
    # print(C_list)
    print(C_overhead)

    # Scaled to payload
    print("MTOW scaled to payload: ", MTOW / W_PL * 250)
    print("Unit cost scaled to payload: ", C_unit / W_PL * 250)
    print("Required energy scaled to payload: ", E_total / W_PL * 250)

# Get the estimate for the power required in cruise.
# Ran = np.linspace(0.7, 1.5, 25)
# Ns_prop = np.array([1, 2, 4, 8, 12, 16, 18, 24, 32])
# Masses_bat = np.empty([len(Ran),len(Ns_prop)])
#
# for j in range(len(Ns_prop)):
#     N_prop = Ns_prop[j]
#     for i in range(len(Ran)):
#         R_prop = Ran[i]
#         print(R_prop)
#         omega_prop = 1500 / R_prop
#         P_cruise = PowerEstimatinonFun(R_prop, N_prop, V_cr, omega_prop, rho, g, M_MTOW)
#         M_bat = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_cruise)
#         Masses_bat[i,j] = M_bat
#         print(R_prop, M_bat)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# Y = Ran; X = Ns_prop
# X, Y = np.meshgrid(X, Y)
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# surf = ax.plot_surface(X, Y, Masses_bat, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=True)
# ax.set_zlim(0, 1000)#
# plt.show()

