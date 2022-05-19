clear all
close all
clc

%%% Not used any more

m = 100; %kg
g = 9.81; %m/s
W = m*g; %N

T = 1; % test for push via matlab
%hey it's German

s=tf([1,0],[1]);
H_0 = 1/(m*s^2);
kpid = pidtune(H_0, 'PID');
fpid1 = feedback(kpid*H_0,1);
Kp = 502;
Ki = 29.1;
Kd = 2.17e+03;


rho = 0.991;
C_D = 0.2;
S = 4.5;
