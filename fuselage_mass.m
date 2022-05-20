function [W_fg] = fuselage_mass(MTOW, V_cr)
inputs;
%global S_nac, N_nac, W_PL, D, l, l_t

% Fuselage mass
% Assume fuselage to be an ellipse of revolution and calculate its wetted area
S_body = np.pi^2 * l * D / 4;
k_wf = 0.23;
V_D = 2*V_cr / 3.6;
W_f = (k_wf * np.sqrt(V_D * (l_t/(D + D))) * S_body^1.2) * 0.45359;

% Furnishing mass
W_fur = 5.9 * (W_PL/125) + 2.3;

% Landing gear mass
k_uc = 1.0;
A_m = 9.1; 
B_m = 0.082; 
C_m = 0.019;
A_n = 11.3; 
C_n = 0.0024;
W_uc_m = k_uc * (A_m + B_m*W_MTOW^0.75 + C_m * MTOW);
W_uc_n = k_uc * (A_n +  + C_n * MTOW);
W_uc = W_uc_n + W_uc_m;

% Nacelle mass
V_D = 2*V_cr;
W_nac = 0.405 * np.sqrt(V_D) * (S_nac^1.3) * N_nac;

% Avionics mass
W_av = 18.1 + 0.008 * MTOW;

W_fg = W_f + W_fur + W_uc + W_nac + W_av;


end