clear all
close all
clc

% global l_pyl R_pyl 

inputs;

n_iter = 10;
for i=1:n_iter
    
    % Thrust power estimation
    [P_cruise, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr);
    
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    P_cont_max = power_from_thrust(dist_force, R_cont, N_cont);
    
    % Weight estimation
    [BatWt, E_total] = BatteryMassFun(V_cr, V_TO, h_TO);
    [PropWt, ~] = propulsiongroup_mass(N_prop, R_prop, B_prop, P_TOL);
    [FuseWt, ~] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, ~] = controlgroup_mass(N_cont, R_cont, B_cont, P_cont_max);
    % TODO: W_beams
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt;

disp("Battery volume: ", V_bat)
disp("Battery weight: ", BatWt)
disp("MTOW: ", MTOW)
disp("Required energy: ", E_total)

disp("For N = ", N_prop, " and R = ", R_prop, ": P_cruise = ", P_cruise, " and P_TOL = ", P_TOL)

end