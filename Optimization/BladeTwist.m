function [outputArg1,outputArg2] = BladeTwist(RPM, R_emp, C_emp, T_cr, rho_emp)

inputs;

sigma = (R_emp * C_emp * B_prop) / (pi * R_emp^2);  % solidity ratio
omega = RPM * 2 * pi / 60;
C_T_sigma = T_cr / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);  % Blade pitch optimized for cruise
theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2)) * (pi/180);  % rad
end

