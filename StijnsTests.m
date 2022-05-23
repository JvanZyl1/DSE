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
y3 = [];
p0s = [];
pis = [];
pps = [];
for i = 1:170
    V_cr_man = (i+80)/3.6;
    RC_AoAandThrust(V_cr_man, MTOW);
    [y(i)] = BatteryMassFun(V_cr_man, V_TO, h_TO);
    [x(i)] = V_cr_man*3.6;
    [y2(i),~,~] = PowerReq(MTOW,V_cr_man);
    [y3(i),~,~,~] = PowerViaDrag(V_cr_man, MTOW);
    [~,p0s(i),~,~] = (PowerViaDrag(V_cr_man, MTOW));
    [~,~,pis(i),~] = PowerViaDrag(V_cr_man, MTOW);
    [~,~,~,pps(i)] = PowerViaDrag(V_cr_man, MTOW);
end
figure(1)
plot(x,y)
figure(2)
plot(x,y2/1000)
figure(3)
hold on
plot(x,y3)
plot(x,p0s/1000)
plot(x,pis/1000,'--')
plot(x,pps/1000,':')
hold off