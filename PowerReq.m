function [P_cruise,P_TOL,P_cont] = PowerReq(MTOW, V_cr_man)
%disp(V_cr_man)
inputs;
%MTOW = 650;    keep these such that function can be tested independently
%when uncommented
%V_cr_man = V_cr;
%required power for cruise and for takeoff
T = (MTOW * g) * 1.1;
[Cruise_ang_rad,~] = RC_AoAandThrust(V_cr_man, MTOW) ;  %obtian cruise angle
kappa = 1.2   ;    %correction factor for extra power losses, value taken from literature
V_perp = (V_cr_man * sin(Cruise_ang_rad)) ;     %perpendicular to rotor plane free stream velocity in [m/s]
%v_i = sqrt((T/A_disk) * (1/(2 * rho)))     ;      %nduced velocity during hover
P = T*V_perp + kappa * T * (-V_perp/2 + sqrt(V_perp^2 / 4 + T/(2 * rho * A_disk))) ; %Preq, cruise
P_cruise = P / eta_final   ;     %efficiency correction
K_TO = 1.5  ;   %safety factor takeoff
T_TOL = K_TO * T  ;    
P_TOL = (((T_TOL * V_TO)/2) * (sqrt(1+(2 * T_TOL)/(rho * V_TO^2 * A_disk))))/eta_final ; %takeoff power

T_cont = 0.5 * CY * rho * V_wind_avg^2 * S_side;  %Thrust req control
P_cont = (((T_cont * V_wind_avg)/2) * (sqrt(1+(2 * T_cont)/(rho * V_wind_avg^2 * A_disk_cont))))/eta_final; %power req  control

end
