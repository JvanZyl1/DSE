function [W_cg, W_cb, W_cm] = controlgroup_mass(P_cont)
inputs;
% Control blades mass per propeller
k_p = 0.124;
D_cont = 2 * R_cont;
P_hp = P_cont * 0.00134102 / N_cont;
W_cb = k_p * (D_cont * P_hp * sqrt(B_cont))^0.78174 * N_cont;

% Control motor mass per motor
W_cm = (P_cont / PowWtRat);

W_cg = W_cb + W_cm;

fprintf('Control motors: %f [kg] \n Control blades: %f [kg] \n', W_cm, W_cb);

end