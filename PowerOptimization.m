clear all
close all
clc

% global l_pyl R_pyl N_prop D

inputs;

n_iter = 10;
for i in range(n_iter):
    
    % Thrust power estimation
    [P_cruise, P_TOL, P_cont] = PowerReq(MTOW, N_prop, R_prop, V_cr, V_TO);
    
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    F_side_avg = 0.5 * 0.6 * rho * V_wind_avg^2 * l * h;
    P_cont_avg = power_from_thrust(F_side_avg, R_cont, N_cont);
    P_cont_max = power_from_thrust(F_side_max, R_cont, N_cont);
    
    % Weight estimation
    BatWt, BatWts, E_total, V_bat = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, P_cont_avg, nu_discharge);
    PropWt, PropWts = PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL);
    FuseWt, FuseWts = FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac);
    ContWt, ContWts = control_group_mass(N_cont, R_cont, B_cont, P_cont_max);
    Weights = np.vstack((BatWts, PropWts, FuseWts, ContWts));
    W_beams = kg_per_m_beam * ((1 * 4 + 0.6 * 2) + (2 * 2 + 1 * 2));
    MTOW = np.sum([PropWt, FuseWt, BatWt, ContWt, W_PL, W_beams]);

disp("Battery volume: ", V_bat)
disp("Battery weight: ", BatWt)
disp("MTOW: ", MTOW)
disp("Required energy: ", E_total)

print("For N = ", N_prop, " and R = ", R_prop, ": P_cruise = ", P_cruise, " and P_TOL = ", P_TOL)



end