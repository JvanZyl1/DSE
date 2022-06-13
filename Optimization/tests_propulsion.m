clear all
close all
clc

inputs;
MTOW = 920;
%[RPM_opt] = LiftDistributionCruise(MTOW);

%%%%%%%% NOW CHANGED FOR VALIDATION %%%%%%%%%%%%%%%
[L] = tipvalidation(MTOW);
%disp(RPM_opt_list)

%[SPL_mat] = NoiseCalculation(MTOW);


