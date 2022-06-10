function [P_cruise,P_TOL] = PowerReq(MTOW,N_prop,R_prop,V_cr)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
T = (MTOW * g) * 1.1;
[CD0, D_q_tot_x] = parasite_drag()   ;
Cruise_ang_rad = RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g) ;
tilt_cruise = Cruise_ang_rad(1)*180/pi  ;     %angle of tilt during cruise in degree
disk_area = R_prop^2 * pi * N_prop ;
kappa = 1.2   ;    %correction factor for extra power losses, value taken from literature
V_perp = (V_cr * np.sin(tilt_cruise * (pi/180))) ;     %perpendicular to rotor plane free stream velocity in [m/s]
%v_i = sqrt((T/disk_area) * (1/(2 * rho)))     ;      %nduced velocity during hover
P = T*V_perp + kappa * T * (-V_perp/2 + sqrt(V_perp^2 / 4 + T/(2 * rho * disk_area))) ;
P_cruise = P / eta_final   ;
K_TO = 1.5  ;   %safety factor takeoff
T_TOL = K_TO * T  ;
P_TOL = (((T_TOL * V_TO)/2) * (np.sqrt(1+(2 * T_TOL)/(rho * V_TO^2 * disk_area))))/eta_final  ;
end