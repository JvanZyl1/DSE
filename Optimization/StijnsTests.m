clear all
close all
clc

%global l_pyl R_pyl N_prop D

inputs;

MTOW = 850;
RPM = 800;
parasite_drag();
%RC_AoAandThrust(V_cr, MTOW);

[P_cruise, P_TOL,P_cont_avg, P_cont_max, P0, Pi, Pp] = PowerReq(MTOW, V_cr, RPM);
[W_bat, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
fprintf('battery weight is %f [kg]',W_bat)

%P_to = P_takeoff/1000
%P_cr = P_CR/1000
%[W_bat, ~] = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, nu_discharge)
%{
x = [];
y = [];     %battery weight midterm method (not necessarily wrong)
y2 = [];    %Power required for cruise midterm method
y3 = [];    %Power required drag method
p0s = [];   %Parasite power
pis = [];   %Induced power
pps = [];   %Profile drag (profile and parasite might be switched)
y4 = [];    %battery weight using new power required method (with drags) 
for i = 1:170
    V_cr_man = (i+80)/3.6;
    RC_AoAandThrust(V_cr_man, MTOW);
    [P_cruise,P_TOL,P_cont] = PowerReq(MTOW, V_cr);
    [y(i),~] = BatteryMassFun(V_cr_man, P_cruise, P_TOL, P_cont);
    [x(i)] = V_cr_man*3.6;
    [y2(i),~,~] = PowerReq(MTOW,V_cr_man);
    [y3(i),p0s(i),pis(i),pps(i)] = PowerViaDrag(V_cr_man, MTOW);
    [y4(i),~] = BatteryMassViaDrag(V_cr_man, MTOW);
    
end
figure(1)
plot(x,y,x,y4,'--')
xlabel('Cruise speed [km/hr]')
ylabel('Battery weight [kg]')
figure(2)
plot(x,y2/1000,x,y3,'--')
figure(3)
hold on
plot(x,y3)
plot(x,p0s/1000)
plot(x,pis/1000,'--')
plot(x,pps/1000,':')
hold off


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

%[C_unit, ~, ~] = CostEstimation((MTOW - (BatWt + PropWt + W_PL)), E_total, P_TOL);

%Battery program


N_cells_series = ceil(Voltage/Cell_volt);
Amp_req = P_TOL/Voltage;
N_cells_para = ceil(Amp_req/Cell_amp);
N_cells = N_cells_para*N_cells_series;
Batweight_cells = N_cells * CellToPack * Cell_mass;
Capacity = N_cells * Cell_capa;
Batvol = Capacity / En_Dens_vol;
fprintf('cells in series:%f ,cells in parallel:%f , total nr of cells:%f \n',N_cells_series,N_cells_para,N_cells)
fprintf('Battery weight: %f [kg]\n',Batweight_cells)
fprintf('Battery volume: %f [L]\n',Batvol)
%}





