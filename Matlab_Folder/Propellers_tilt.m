clear all
close all
clc

h = 0.1; % Height of prop
h_mass_prop = 0.5; %Where the prop_cg is placed in relation to prop height
theta_0 = [0; 0; 0]; %Initial angle
theta_final = [pi; 0; 0]; %Final angle
w_0 = [0;0;0];
T_prop = 500;
I_mat = [2 10 0 ;
    0 10 0;
    0 0 10];
I_inv = inv(I_mat);