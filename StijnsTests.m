clear all
close all
clc

%global l_pyl R_pyl N_prop D

inputs;


parasite_drag();


%[~,P_takeoff,~] = PowerReq(MTOW,V_cr);
%[P_CR,~,~] = PowerReq(MTOW,V_cr);
%P_to = P_takeoff/1000
%P_cr = P_CR/1000
%[W_bat, ~] = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, nu_discharge)
x = [];
y = [];
x2 = [];
y2 = [];
for i = 1:200
    V_cr_man = (i+100)/3.6;
    RC_AoAandThrust(V_cr_man, MTOW);
    [y(i)] = BatteryMassFun(V_cr_man, V_TO, h_TO);
    [x(i)] = V_cr_man*3.6;
    [cruisepower,~,~] = PowerReq(MTOW,V_cr_man);
    [y2(i)] = cruisepower;
    disp(cruisepower);
end
figure(1)
plot(x,y)
figure(2)
plot(x,y2)
