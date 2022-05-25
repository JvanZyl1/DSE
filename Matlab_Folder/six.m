clear all
close all
clc

I_xx = 1.2;
I_yy = 1.0;
I_zz = 0.5;

Inertia = [I_xx 0 0;
    0 I_yy 0;
    0 0 I_zz];
I_mat = Inertia;
Inertia_inv = inv(Inertia);
I_inv = Inertia_inv;

theta_0 = [0;0;0];
w_0 = [0;0;0];
theta_z_f = pi;
q_0 = [1; 0; 0; 0];

m = 300;
rho = 1.225;
g = 9.81;
T = 10.5;
C_D = 0.6;
time_delay = 0.1;
S = 1*1.8;




%A = eye(3);
%B = [1/m; 1/m; 1/m];
%C = eye(3);
%D = zeros(3);
%sys = ss(A,B,C,D);





