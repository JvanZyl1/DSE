clear all
close all
clc

inputs;

% LiftPowerRPM
[RPM_opt_list, lin_twist] = TipAngleOpt(10000);
%SPL_mat = NoiseCalculation(950);