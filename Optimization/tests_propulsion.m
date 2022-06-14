clear all
close all
clc

inputs;
MTOW = 866;
[RPM_opt] = LiftDistributionCruise(MTOW);
[RPM_opt_list, lin_twist, T_list,V_i_emp] = TipAngleOpt(MTOW);

%%%%%%%% NOW CHANGED FOR VALIDATION %%%%%%%%%%%%%%%
%[L] = tipvalidation(MTOW);
%disp(RPM_opt_list)

[SPL_mat] = NoiseCalculation(MTOW);


