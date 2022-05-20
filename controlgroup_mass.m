function [W_cg, W_cb, W_cm] = controlgroup_mass(N_cont, R_cont, B_cont, P_cont)
inputs;
% Control blades mass per propeller
k_p = 0.124;
D_cont = 2 * R_cont;
P_hp = P_cont * 0.00134102 / N_cont;
W_cb = k_p * (D_cont * P_hp * np.sqrt(B_cont))^0.78174;

% Control motor mass per motor
W_cm = (P_TOL / PowWtRat) / N_cont;

W_cg = W_cb * N_cont + W_ce * N_cont;

end