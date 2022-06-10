function [P_cruise, P_TOL,P_cont_avg, P_cont_max, P0, Pi, Pp, T_TOL, T_cr] = PowerReq(MTOW, V_cr, RPM)

inputs;

%%%%%%%%%%%% Old approach for power required for cruise %%%%%%%%%%%%
%[Cruise_ang_rad,~] = RC_AoAandThrust(V_cr, MTOW) ;  %obtian cruise angle
%kappa = 1.2   ;    %correction factor for extra power losses, value taken from literature
%V_perp = (V_cr * sin(Cruise_ang_rad)) ;     %perpendicular to rotor plane free stream velocity in [m/s]
%v_i = sqrt((T/A_disk) * (1/(2 * rho)))     ;      %nduced velocity during hover
%P = T*V_perp + kappa * T * (-V_perp/2 + sqrt(V_perp^2 / 4 + T/(2 * rho * A_disk))) ; %Preq, cruise
%P_cruise = P / (eta_final * redundancy_factor)  ;     %efficiency correction

%%%%%%%%%% Power required for cruise %%%%%%%%%%%
parasite_drag();
RC_AoAandThrust(V_cr, MTOW);
omega_prop = RPM * 2 * pi / 60;
K = 4.65  ;         % 4.5 in hover to 5 at mu = .5
sigma = (R_prop * C_prop * B_prop)/(pi*R_prop^2);   % solidity for the main rotor
kappa = 1.15    ;                               % induced power factor
C_d0 = 0.008     ; % profile drag coefficient of the blade
[alpha, ~] = RC_AoAandThrust(V_cr, MTOW);
alpha_TPP = alpha     ;  % angle of attack in cruise [deg]

[~ , D_q_tot_x] = parasite_drag() ;
f = D_q_tot_x        ;                            % equivalent area estimated from reference A/C [m2]
A_rotor = A_disk   ;        % rotor area in [m2]
mu = (V_cr * cos((alpha_TPP))) / (omega_prop * R_prop)   ; % advance ratio [~]
% Calculate the dimensionalizing factor
P_fact =  rho * A_rotor * (R_prop*omega_prop)^3   ;
%    % Caculate the thrust coefficient
T_cr = MTOW * g / cos(deg2rad(alpha_TPP));
C_T = T_cr / (rho * (R_prop * omega_prop)^2 * A_rotor)   ;

C_P0 = sigma * C_d0 * (1 + (K * mu^2)) / 8     ;
P0 = C_P0 * P_fact       ;

% it is assumed that mu >> lambda here
C_Pi = kappa * C_T^2 / (2 * mu)   ; %Induced power coefficient [-]
Pi = C_Pi * P_fact    ;
C_Pp = 0.5 * mu^3 * (f/A_rotor) ;%Parisative power coefficient [-]
Pp = C_Pp * P_fact    ;


P_cruise = (P0 + Pi + Pp)/(eta_final * redundancy_factor)   ; %Total power from components [W]

%%%%%%%%%%% Power required for takeoff and landing %%%%%%%%%%%%
T = (MTOW * g) * 1.1   ;
K_TO = 1.5  ;   %safety factor takeoff
T_TOL = K_TO * T  ;   
P_TOL = (((T_TOL * V_TO)/2) * (sqrt(1+(2 * T_TOL)/(rho * V_TO^2 * A_disk))))/(eta_final * redundancy_factor) ; %takeoff power

%%%%%%%%%%% Power required for the control propellers %%%%%%%%%%%%
% Separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
T_cont_avg = 0.5 * Side_CD_times_S * rho * V_wind_avg^2;
P_cont_avg = (((T_cont_avg * V_wind_avg)/2) * (sqrt(1+(2 * T_cont_avg)/(rho * V_wind_avg^2 * A_disk_cont))))/eta_final; %power req  control

P_cont_max = (((dist_force * V_wind_avg) / 2) * (sqrt(1 + (2 * dist_force) / (rho * V_wind_avg^2 * A_disk_cont))))/eta_final;

end