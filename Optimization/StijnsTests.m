clear all
close all
clc

%global l_pyl R_pyl N_prop D

inputs;

MTOW = 900;
RPM = 800;
parasite_drag();
%RC_AoAandThrust(V_cr, MTOW);

[P_cruise, P_TOL,P_cont_avg, P_cont_max, P0, Pi, Pp, T_TOL, T_cr] = PowerReq(MTOW, V_cr, RPM);
[W_bat, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_max);
fprintf('P_req takeoff: %f [kW], P_req cruise: %f [kW]',P_cruise/1000,P_TOL/1000)




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
%}

%point list
%full charge 5am
% 1 flight at 5am and charge (10 min flight, 10 min loading, 30 min charge) (23433.6 Wh used) 5:50 am !
% 20 minutes of rest/maintenance 6:10
% 1 flight back without payload (17329 Wh used, 10 min flight), then charge (25 min charge) 6:45 am ! 
% 7 am one long flight (10 min flight, 10 loading then 30 min charge) (23433.6 Wh used) 7:50 am !
% 10 minutes rest and maintenance
% 8:00 another flight (10 min, 10 min loading) (23433.6 Wh used)   8:20am !
% Battery swap 10 mins                             8:30 am
% Short flight 15km (7.5 mins, 10 mins loading, 21097.67 Wh used) (30 min charging) 9:20 am !
% 1.5 hrs rest/maintenance due to low traffic    10:50 am
% 





