clear all
close all
clc

%% Generic inputs
I_xx = 3866.543;
I_yy = 16529.205;
I_zz = 17264.21;

Inertia = [I_xx 0 0;
    0 I_yy 0;
    0 0 I_zz];
I_mat = Inertia;
Inertia_inv = inv(Inertia);
I_inv = Inertia_inv;

theta_0 = [0;0;0];
w_0 = [0;0;0];
r_0 = [0;0;0];
v_0 = [0;0;0];
a_0 = [0;0;0];

m = 645;
rho = 1.225;
g = 9.81;
T = 10.5;
C_D = 0.6;
time_delay = 0.1;
S = 1*1.8;

%% Linear Dynamics Inputs
%F_aero = [1;2;3];
r_trajectory = [2;3;4];
%a_accelerometer_error = [1;2;3];


%% Linear Dynamics Kalman Filter

A_kal = [0 0 0 1 0 0;
    0 0 0 0 1 0;
    0 0 0 0 0 1;
    0 0 0 0 0 0;
    0 0 0 0 0 0;
    0 0 0 0 0 0];

B_kal = [0 0 0 0 0 0;
    0 0 0 0 0 0;
    0 0 0 0 0 0;
    0 0 0 1/m 0 0;
    0 0 0 0 1/m 0;
    0 0 0 0 0 1/m];

C_kal = eye(6);

D_kal = zeros(6);

%% Angular dynamics Kalman filter

A_i = vertcat(zeros(3), zeros(3));
A_ii = vertcat(eye(3), zeros(3));
A_AD = horzcat(A_i, A_ii);

B_i = vertcat(zeros(3), zeros(3));
B_ii = vertcat(zeros(3), I_inv);
B_AD = horzcat(B_i, B_ii);



C_AD = eye(6);
D_AD = zeros(6);

sys = ss(A_AD, B_AD, C_AD, D_AD);

%% PID tune of angular shite
A_2 = zeros(3);
B_2 = I_inv;
C_2 = eye(3);
D_2 = zeros(3);
sys2 = ss(A_2, B_2, C_2, D_2)

trans_func = tf(sys2)

pid_Mx = pidtune(trans_func(1,1), 'PID');
pid_Mx = [pid_Mx.Kp, pid_Mx.Ki, pid_Mx.Kd];

pid_My = pidtune(trans_func(2,2), 'PID');
pid_My = [pid_My.Kp, pid_My.Ki, pid_My.Kd];

pid_Mz = pidtune(trans_func(3,3), 'PID');
pid_Mz = [pid_Mz.Kp, pid_Mz.Ki, pid_Mz.Kd];

load('MPCDesignerSession.mat');

%A = eye(3);
%B = [1/m; 1/m; 1/m];
%C = eye(3);
%D = zeros(3);
%sys = ss(A,B,C,D);