clear all
close all
clc

% global l_pyl R_pyl 

inputs;
MTOW = 700;  % kg

n_iter = 100;
for i=1:n_iter
    % Thrust power estimation
    [P_cruise, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr);
    
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    P_cont_max = power_from_thrust(dist_force, R_cont, N_cont);
    
    % Weight estimation
    [BatWt, E_total] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
    [PropWt] = propulsiongroup_mass(P_TOL);
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, ~, ~] = controlgroup_mass(P_cont_max);
    W_beams = 40;  % TODO
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
end


fprintf('Battery weight: %f \n',BatWt)
fprintf('MTOW: %f \n',MTOW)
fprintf('Required energy: %f \n',E_total)
fprintf('P_cruise = %f, and P_TOL = %f \n',P_cruise,P_TOL)