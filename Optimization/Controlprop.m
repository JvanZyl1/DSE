% Parameters set for control propeller

tip_radius = 0.30;
hub_radius = 0.05;
chord = 0.05;
aoa = 10;
L = 0.25;
S = L * chord;
CL = 1.2;
rho = 1.225;

number_blades = 3;
mass_blade = 0.150;
MOI = 1/3 * 0.15 * 0.25^2;
total_MOI = 3 * MOI

peak_torque = 90;
ang_acc = peak_torque / total_MOI


thrust = linspace(0,3000, 31);

T = 1500;
T_blade = T / 9;
omega = (T_blade * 6 / rho / S / CL / L^3)^0.5;
rpm = omega / 2 / 3.14159 * 60
acc_time = omega / ang_acc

% 
% for i=1:length(thrust)
%     T = thrust(i);
%     T_blade = T / 9;
%     omega = (T_blade * 6 / rho / S / CL / L^3)^0.5;
%     acc_time = omega / ang_acc
%     rpm = omega / 2 / 3.14159 * 60
% end
