function [alpha, Treq] = RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g)
'Rotor craft angle of attack estimator';
%Nominal drag force on fuselage during cruise
D = 0.5 * rho * V_cr^2* D_q_tot_x  ;
%Equilibrium AoA ;
alpha = atan2(D,MTOW * g)  ;
Treq = np.sqrt((MTOW*g)^2 + D^2) ;


end