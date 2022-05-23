clear all
close all
clc

% global l_pyl R_pyl 

inputs;
MTOW = 700;  % kg

A_disk_big = R_prop_big^2 * pi * N_prop_big;
A_disk_small = R_prop_small^2 * pi * N_prop_small ;
A_disk = A_disk_big + A_disk_small;
A_disk_cont = R_cont^2 * pi * N_cont;
bigprop_factor = A_disk_big / (A_disk_big + A_disk_small);
smallprop_factor = 1 - bigprop_factor;
disp(A_disk)

n_iter = 100;
for i=1:n_iter
    % Thrust power estimation
    [P_cruise, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr, A_disk, A_disk_cont);
    
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    P_cont_max = power_from_thrust(dist_force, R_cont, N_cont);
    
    % Weight estimation
    [BatWt, E_total] = BatteryMassFun(V_cr, V_TO, h_TO, P_cruise, P_TOL, P_cont_avg);
    [PropWt_big] = propulsiongroup_mass(N_prop_big, R_prop_big, B_prop, P_TOL*bigprop_factor);
    [PropWt_small] = propulsiongroup_mass(N_prop_small, R_prop_small, B_prop, P_TOL*smallprop_factor);
    PropWt = PropWt_big + PropWt_small;
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, ~, ~] = controlgroup_mass(N_cont, R_cont, B_cont, P_cont_max);
    W_beams = 40;  % TODO
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
end


fprintf('Battery weight: %f \n',BatWt)
fprintf('MTOW: %f \n',MTOW)
fprintf('Required energy: %f \n',E_total)
fprintf('P_cruise = %f, and P_TOL = %f \n',P_cruise,P_TOL)