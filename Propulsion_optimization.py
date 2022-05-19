import numpy as np
from PowerEstimation import *
from MassEstimation import *
from PropulsionMethods import *
from inputs import *

for N_prop in [10]:

    R_prop = np.sqrt(A_disk / N_prop / np.pi)

    n_iter = 10
    for i in range(n_iter):

        # Thrust power estimation
        P_cruise = PowerReq(MTOW, N_prop, R_prop, V_cr, V_TO)[0]
        P_TOL = PowerReq(MTOW, N_prop, R_prop, V_cr, V_TO)[1]

        # Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
        F_side_avg = 0.5 * 0.6 * rho * V_wind_avg**2 * l * h
        P_cont_avg = power_from_thrust(F_side_avg, R_cont, N_cont)
        P_cont_max = power_from_thrust(F_side_max, R_cont, N_cont)
        print(P_cont_max, MTOW)

        # Weight estimation
        BatWt, BatWts, E_total = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, P_cont_avg, nu_discharge)
        PropWt, PropWts = PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL)
        FuseWt, FuseWts = FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac)
        ContWt, ContWts = control_group_mass(N_cont, R_cont, B_cont, P_cont_max)
        Weights = np.vstack((BatWts, PropWts, FuseWts, ContWts))
        MTOW = np.sum([PropWt, FuseWt, BatWt, ContWt, W_PL])

    print("Battery weight: ", BatWt)
    print("MTOW: ", MTOW)
    print("Required energy: ", E_total)

    print("For N = ", N_prop, " and R = ", R_prop, ": P_cruise = ", P_cruise, " and P_TOL = ", P_TOL)

