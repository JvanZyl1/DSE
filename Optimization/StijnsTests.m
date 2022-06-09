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


%{
p1 = Capacity;
p2 = Capacity - ((0.5* t_TO/3600) * P_TOL)*redundancy_factor;
p3 = p2 - ((t_cr/3600) * P_cruise)*redundancy_factor;
p4 = p3  - ((0.5* t_TO/3600) * P_TOL)*redundancy_factor;
x1 = 0;
x2 = t_TO/2;
x3 = x2 + t_cr;
x4 = x3 + t_TO/2;

Xs = [x1,x2/60,x3/60,x4/60];
Ys = [p1/1000,p2/1000,p3/1000,p4/1000];
plot(Xs,Ys)
%}


%P_to = P_takeoff/1000
%P_cr = P_CR/1000
%{
x = [];
y = [];     %battery weight midterm method (not necessarily wrong)
 
for i = 1:200
    V_cr_man = (i+50)/3.6;
    RC_AoAandThrust(V_cr_man, MTOW);
    [P_cruise, P_TOL,P_cont_avg, P_cont_max, P0, Pi, Pp, T_TOL, T_cr] = PowerReq(MTOW, V_cr_man, RPM);
    P_cont = P_cont_avg;
    [y(i),~,~] = BatteryMassFun(V_cr_man, P_cruise, P_TOL, P_cont);
    [x(i)] = V_cr_man*3.6;
    disp(x(i))
    
    
end
figure(1)
plot(x,y)
xlabel('Cruise speed [km/hr]')
ylabel('Battery weight [kg]')
disp(min(y))



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







