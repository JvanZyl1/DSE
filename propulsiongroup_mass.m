function [W_pg, W_m, W_b, W_c] = propulsiongroup_mass(P_TOL)
inputs;
% Global PowWtRat
%disp([PowWtRat, P_TOL, N_prop])

% Motor mass per motor
W_m = (P_TOL / PowWtRat) / N_prop;

% Propeller blade mass per propeller
k_p = 0.124;
D_prop = 2 * R_prop;
P_hp = P_TOL * 0.00134102 / N_prop;
W_b = k_p * (D_prop * P_hp * sqrt(B_prop))^0.78174;

% Cable mass
rho_c = 0.3;
l_cab = R_prop + 2;
W_c = ( rho_c * (l_cab * 2) );

W_pg = (W_m + W_b + W_c) * N_prop;

fprintf('Per motor: %f [kg] \n Blades per prop: %f [kg] \n Cables per prop: %f [kg] \n', W_m, W_b, W_c);

end
