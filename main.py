'''Conceptual Design of the Urban Air Vehicle'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from inputs import *
from PowerEstimation import *
from MassEstimation import *

#P_cruise = PowerEstimationFun(R_prop, N_prop, V_cr, omega_prop, rho, g, W_MTOW)

# Weight Estimation routine for KittyHawk
BatWt, BatWts = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_cruise)
PropWt, PropWts = PropGroupMassFun(N_prop, R_prop, B_prop, P_cruise)
WingWt, WingWts = WingGroupMassFun(W_MTOW, W_PL, b, S, n_ult)
FuseWt, FuseWts = FuselageGroupMassFun(W_MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac)
TailWt, TailWts = TailplaneGroupFun(W_MTOW, S_h, t_rh, t_rv, Lambda_v, A_v, A_h)
Weights = np.vstack((BatWts,PropWts,WingWts,FuseWts,TailWts))
print(Weights)
print(np.sum([PropWt,WingWt,FuseWt,TailWt,BatWt,W_PL]))
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
