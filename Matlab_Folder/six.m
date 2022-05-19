clear all
close all
clc

I_xx = 1.2;
I_yy = 1.0;
I_zz = 0.5;

Inertia = [I_xx 0 0;
    0 I_yy 0;
    0 0 I_zz];

Inertia_inverse = inv(Inertia);

theta_0 = [0;0;0];
w_0 = [0;0;0];
theta_z_f = pi;
q_0 = [1; 0; 0; 0];

T_max = 5000; %Nm
dwx = T_max/I_xx;
dwy = T_max/I_yy;
dwz = T_max/I_zz;



