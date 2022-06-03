clear all
close all
clc

alpha = [-2, -2, -2, -1.5, -0.8, -0.5, 1, 5, 10, 20, 25];
Cl_arr = [0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 0];
disp(Cl_arr(alpha<10 & alpha>-1))

r = 0.1:0.1:1.2;
disp(r)
