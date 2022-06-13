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
% 1 long flight 20km, half payload (10 min loading, 10 min flying)(20259 Wh used)(25min charging) 11:35!
% low traffic until 4:00 pm
% 1 long flight 20km (10 min loading, 10 min flying)(23433.6 Wh used)(30min charging) 4:50 pm!
% Rest until 6:00 pm
% 1 short flight 10 km (10 min loading, 5 min flying)(18761.757 Wh used)(20 min charging) 6:45 pm!
% immediately new flight 20km (10 min loading, 10 min flying)(23433.6 Wh used)(20 min charging up to 80%) 7:25 pm!
% Final flight 20km (10 min loading, 10 min flying)(23433.6 Wh used) 7:45 pm! 
% charging back to 100% (50 min)
% rest of day for maintenance

%{
Whtot = vol_dens * V_bat;
x = [];
y = [];
y(1) = 1;
x(1) = 4.5;
y(2) = 1;
x(2) = 5 + 5/60;
y(3) = 1 - 23433.6/Whtot;
x(3) = x(2) + 1/6;
y(4) = 1;
x(4) = x(3) + 5/60 + 30/60;
y(5) = 1;
x(5) = x(4) + 20/60 + 5/60;
y(6) = 1 - 17329/Whtot;
x(6) = x(5) + 10/60;
y(7) = 1;
x(7) = x(6) + 20/60;
y(8) = 1 ;
x(8) = 7 + 5/60;
y(9) = 1 - 23433.6/Whtot;
x(9) = x(8) + 15/60;
y(10) = 1;
x(10) = x(9) + 30/60;
y(11) = 1;
x(11) = x(10) + 10/60 + 5/60;
y(12) = 1 - 23433.6/Whtot;
x(12) = x(11) + 15/60;
y(13) = y(12);
x(13) = x(12) + 5/60;
y(14) = 1;
x(14) = x(13);
y(15) = 1;
x(15) = x(14) + 10/60;
y(16) = 1- 21097.67/Whtot;
x(16) = x(15) + 5/60 + 10/60;
y(17) = 1;
x(17) = x(16) + 30/60;
y(18) = 1;
x(18) = x(17) + 1.5 + 5/60;
y(19) = 1 - 20259/Whtot;
x(19) = x(18) + 5/60 + 10/60;
y(20) = 1;
x(20) = x(19) + 25/60;
y(21) = 1;
x(23) = 1 + 12 + 5/60;
y(22) = 1 - 23433.6/Whtot;
x(21) = x(20) + 15/60;
y(23) = 1;
x(22) = x(21) + 30/60;
y(24) = 1;
x(24) = 18 + 5/60;
y(25) = 1 - 18761.757/Whtot;
x(25) = x(24) + 10/60;
y(26) = 1;
x(26) = x(25) + 20/60;
y(27) = 1;
x(27) = x(26) + 5/60;
y(28) = 1 - 23433.6/Whtot;
x(28) = x(27) + 15/60;
y(29) = 0.8;
x(29) = x(28) + 20/60 + 6/50;
y(30) = 0.8;
x(30) = x(29) + 5/60;
y(31) = 0.8 - 23433.6/Whtot;
x(31) = x(30) + 15/60;
y(32) = 1;
x(32) = x(31) + 50/60;
y(33) = 1;
x(33) = 22;
plot(x,y*100)
axis([4.5 22 0 105])
xlabel('Time Throughout Day [hr]','FontSize',13)
ylabel('Charge level in %','FontSize',14')
%}






