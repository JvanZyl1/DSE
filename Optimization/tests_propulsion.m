clear all
close all
clc

inputs;
MTOW = 930;
[RPM_opt] = LiftDistributionCruise(MTOW);
[RPM_opt_list, lin_twist, T_list,V_i_emp] = TipAngleOpt(MTOW);

fprintf('Cruise = %f, Take-off = %f, Landing = %f \n', RPM_opt, RPM_opt_list)

%%%%%%%% NOW CHANGED FOR VALIDATION %%%%%%%%%%%%%%%
%[L] = tipvalidation(MTOW);
%disp(RPM_opt_list)

%[SPL_mat] = NoiseCalculation(MTOW);



% 91.8 vs 85.1
% 75 vs 80

