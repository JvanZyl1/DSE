clear all
close all
clc

% global l_pyl R_pyl 

inputs;
MTOW = 700;  % kg
%V_cr = 180 / 3.6 ; % Cruise velocity [m/s]

n_iter = 10;
%for i=1:n_iter
%    % Thrust power estimation
%    [P_cruise, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr);
%    
%    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
%    P_cont_max = (((dist_force * V_wind_avg) / 2) * (sqrt(1 + (2 * dist_force) / (rho * V_wind_avg^2 * A_disk_cont)))) / eta_final;
%    
%    % Weight estimation
%    [BatWt, E_total] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
%    [PropWt] = propulsiongroup_mass(P_TOL);
%    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
%    [ContWt, ~, ~] = controlgroup_mass(P_cont_max);
%    W_beams = 60;  % TODO
%    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
%end

%%%%%%%%%%%% MTOW ESTIMATION with new power estimation method %%%%%%%%%%%
% for V_cr in V_cr_list
for i=1:n_iter
    % Thrust power estimation
    [P_cruise, P_TOL,P_cont_avg, P_cont_max, ~, ~, ~] = PowerReq(MTOW, V_cr);
    
    % Weight estimation
    [BatWt, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
    [PropWt, W_m, W_b, W_c] = propulsiongroup_mass(P_TOL);
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, W_cm, W_cb] = controlgroup_mass(P_cont_max);
    W_p = W_m + W_b;
    [W_beams] = StructureOptimization(MTOW, W_p);
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
    %disp([W_PL, BatWt, PropWt, FuseWt, ContWt, W_beams])
end

[C_unit, ~, ~] = CostEstimation((MTOW - (BatWt + PropWt + W_PL)), E_total, P_TOL);

%fprintf('MTOW: %f [kg]\n',MTOW)
%fprintf('Battery weight: %f [kg]\n',BatWt)
%fprintf('Required energy: %f [Wh]\n',E_total)
%fprintf('Battery volume: %f [L]\n', V_bat)
%fprintf('P_cruise = %f [W], and P_TOL = %f [W]\n',P_cruise,P_TOL)
%fprintf('The total cost per vehicle: = %f [€]', C_unit)

%%%%%%%%% RPM Calculation %%%%%%%%%%%%%%
RPM_list = 500:100:1500;
LiftPowerRPM(MTOW, RPM_list);



%%%%%%%%% Angular acceleration calculation %%%%%%%%%%%
Ang_acc_prop = angular_acc(W_m, W_b, B_prop, R_prop);
Ang_acc_cont = angular_acc(W_cm, W_cb, B_cont, R_cont);
%fprintf('Angular acceleration for propellers: %f [rad/s^-2]\nAngular acceleration for control props: %f [rad/s^-2]\n', Ang_acc_prop, Ang_acc_cont)

%%%%%%%%% Reynold's number calculation %%%%%%%%%%%%%
omega_list = 500:100:1000;
r_list = 0:0.06:R_prop;

for omega_prop=omega_list
    for r=r_list
        V = r * omega_prop * 2 * pi / 60; 
        if V>265
            %fprintf('Tip speed exceeds 0.8M at r = %f \n', r)
            break
        end
        Re = rho * V * C_prop / (1.81 * 10^(-5));
        %disp(r/0.12);
        %disp(Re);
        if r==R_prop
            %fprintf('Tip speed does not exceed 0.8M at %i RPM \n', omega_prop)
        end
    end
end



