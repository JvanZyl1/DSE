clear all
close all
clc

h = 0.1; % Height of prop
h_mass_prop = 0.5; %Where the prop_cg is placed in relation to prop height
theta_0 = [0; 0; 0]; %Initial angle
theta_final = [pi; 0; 0]; %Final angle
w_0 = [0;0;0];
T_prop = 500;
I_mat = [1.5 0 0 ;
    0 0.4 0;
    0 0 0.4];
I_diag = diag(I_mat);
I_inv = inv(I_mat);
I_inv = diag(I_mat);
I_mat = I_diag;
T = 0.1;
w_p_0 = 90*pi/(180*T);
w_s_0 = 650;
w_p_dot = 0;
w_s_dot = 0;
psI_dot = 0;
psI_0 = 0;
