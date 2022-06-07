clear all
close all
clc

inputs;

MTOW = 900;  % kg, initial MTOW estimation
RPM_cr = 1000; % initial RPM estimation
%RPM_list = 100:100:2000;  % RPM range to iterate on
n_iter = 10;
for i=1:n_iter

    % Power calculation
    [P_cruise, P_TOL,P_cont_avg, P_cont_max, P0, Pi, Pp, T_TOL, T_cr] = PowerReq(MTOW, V_cr, RPM_cr);
    
    % Weight estimation
    [BatWt, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
    [PropWt, W_m_avg, W_b, W_c] = propulsiongroup_mass(P_TOL, MTOW);
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, W_cm, W_cb] = controlgroup_mass(P_cont_max);
    W_p = W_m_avg + W_b;
    [W_beams] = StructureOptimization(MTOW, W_p);
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
    disp(MTOW)
    %disp([W_PL, BatWt, PropWt, FuseWt, ContWt, W_beams])

    % RPM and blade twist approximation
    %[RPM_opt_list, lin_twist] = LiftPowerRPM(MTOW, T_cr);
    [RPM_opt_list, lin_twist, T_list] = TipAngleOpt(MTOW);
    RPM_cr = RPM_opt_list(1);

end

[SPL_list] = NoiseCalculation(MTOW, RPM_opt_list);

[C_unit, ~, ~] = ParametricCostEstimation((MTOW - (BatWt + PropWt + W_PL)), E_total, P_TOL);

fprintf('MTOW: %f [kg]\n',MTOW)
%fprintf('Battery weight: %f [kg]\n',BatWt)
fprintf('Required energy: %f [Wh]\n',E_total)
%fprintf('Battery volume: %f [L]\n', V_bat)
%fprintf('P_cruise = %f [W], and P_TOL = %f [W]\n',P_cruise,P_TOL)
%fprintf('The total cost per vehicle: = %f [€]\n', C_unit)
fprintf('Linear twist = %f, RPM = %f, %f, %f, %f \n', lin_twist, RPM_opt_list)















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

