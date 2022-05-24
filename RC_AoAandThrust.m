function [alpha, Treq] = RC_AoAandThrust(V_cr_man, MTOW)
inputs;
%MTOW = 700;
%V_cr_man = V_cr;
parasite_drag();
[CD0, D_q_tot_x] = parasite_drag();
%global V_cr D_q_tot_x rho MTOW g 
'Rotor craft angle of attack estimator';
%Nominal drag force on fuselage during cruise
D = 0.5 * rho * V_cr_man^2* D_q_tot_x  ;
%Equilibrium AoA ;
alpha = atan2(D,MTOW * g)  ;
Treq = sqrt((MTOW*g)^2 + D^2) ;
alpha

end