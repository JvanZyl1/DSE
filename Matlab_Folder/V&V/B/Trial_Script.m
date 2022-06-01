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

%% PID tune of angular 
A_2 = zeros(3);
B_2 = I_inv;
C_2 = eye(3);
D_2 = zeros(3);
sys2 = ss(A_2, B_2, C_2, D_2);

trans_func = tf(sys2)

pid_Mx = pidtune(trans_func(1,1), 'PID');
pid_Mx = [pid_Mx.Kp, pid_Mx.Ki, pid_Mx.Kd];

pid_My = pidtune(trans_func(2,2), 'PID');
pid_My = [pid_My.Kp, pid_My.Ki, pid_My.Kd];

pid_Mz = pidtune(trans_func(3,3), 'PID');
pid_Mz = [pid_Mz.Kp, pid_Mz.Ki, pid_Mz.Kd];

v_vehicle = [20; 0; 0];
theta_vehicle = [0;0; 0];
x_cp = [0.3; 0.2; 0.1];

K_gain = 300; %10000
a_MF = 0.6; %2.5
c_MF = 1.5; %1.75

load('MPCDesignerSession.mat');
%{
a_list = [];
K_list = [];
c_list = [];
angerror_list =[];
Mc_list =[];
radx_list = [];
rady_list = [];
radz_list = [];
xe_list =[];
ye_list = [];
ze_list = [];
for i = 0:1 %c_MF
    i = i/10;
    c_MF = i;
    for j = 5:5:40 %a_MF
        j = j/10;
        a_MF = j;
        for k = 3 %K_gain
            i
            k = k*100;
            K_gain = k;
            sim('simgoid_terry.slx', 60);
            c_list = [c_list; i];
            a_list = [a_list; j];
            K_list = [K_list; k];
            Mc_list = [Mc_list; ans.Mc];
            angerror_list = [angerror_list; ans.angle_error];
            radx_list = [radx_list, ans.radx];
            rady_list = [rady_list, ans.rady];
            radz_list = [radz_list, ans.radz];
            length(ans.errorx);
            %xe_list = [xe_list, ans.errorx];
            %ye_list = [ye_list, ans.errory];
            %ze_list = [ze_list, ans.errorz];
        end
    end
end
%}      

