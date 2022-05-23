function [P_cruise,P_TOL,P_cont] = PowerReq(MTOW, V_cr, A_disk, A_disk_cont)
%disp(V_cr)
inputs;

%global  g rho V_TO eta_final 
%required power for cruise and for takeoff
%   Detailed explanation goes here
T = (MTOW * g) * 1.1;
%[CD0, D_q_tot_x] = parasite_drag()   ;
Cruise_ang_rad = RC_AoAandThrust(V_cr, MTOW) ;
tilt_cruise = Cruise_ang_rad(1)*180/pi  ;     %angle of tilt during cruise in degree
kappa = 1.2   ;    %correction factor for extra power losses, value taken from literature
V_perp = (V_cr * sin(tilt_cruise * (pi/180))) ;     %perpendicular to rotor plane free stream velocity in [m/s]
%v_i = sqrt((T/A_disk) * (1/(2 * rho)))     ;      %nduced velocity during hover
P = T*V_perp + kappa * T * (-V_perp/2 + sqrt(V_perp^2 / 4 + T/(2 * rho * A_disk))) ;
P_cruise = P / eta_final   ;
K_TO = 1.5  ;   %safety factor takeoff
T_TOL = K_TO * T  ;
P_TOL = (((T_TOL * V_TO)/2) * (sqrt(1+(2 * T_TOL)/(rho * V_TO^2 * A_disk))))/eta_final  ;
P_cont = (((dist_force * V_wind_avg)/2) * (sqrt(1+(2 * dist_force)/(rho * V_wind_avg^2 * A_disk_cont))))/eta_final;

end
