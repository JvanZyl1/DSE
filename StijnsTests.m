clear all
close all
clc

%global l_pyl R_pyl N_prop D

inputs;


parasite_drag();
RC_AoAandThrust(V_cr, rho, MTOW, g);


[~,P_takeoff,~] = PowerReq(MTOW,V_cr);
[P_CR,~,~] = PowerReq(MTOW,V_cr);
P_to = P_takeoff/1000
P_cr = P_CR/1000
[W_bat, ~] = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, nu_discharge)
for V_test = 100:200
    [y,~,~] = PowerReq(MTOW,V_test);
    y
end
