function [W_pg] = propulsiongroup_mass(N_prop, R_prop, B_prop, P_TOL)
inputs;
% Global PowWtRat

% Motor mass per motor
W_m = (P_TOL / PowWtRat) / N_prop;

% Propeller blade mass per propeller
k_p = 0.124;
D_prop = 2 * R_prop;
P_hp = P_TOL * 0.00134102 / N_prop;
W_b = k_p * (D_prop * P_hp * np.sqrt(B_prop))^0.78174;

% Cable mass
W_e_ref = 10;
l_cab = R_prop + 2;
W_c = ( W_e / W_e_ref * (l_cab * 2) ) * N_prop;

W_pg = W_m + W_b + W_c;

end