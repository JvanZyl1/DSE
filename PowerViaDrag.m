function [cruisepower,P0,Pi,Pp] = PowerViaDrag(V_cr_man, MTOW)
%UNTITLED2 Summary of this function goes here
%Detailed explanation goes here
inputs;
%V_cr_man = V_cr;
parasite_drag();
RC_AoAandThrust(V_cr_man, MTOW);
% Assumed values for power estimation

K = 4.65  ;                                     % 4.5 in hover to 5 at mu = .5
sigma = 0.1   ;                                 % solidity for the main rotor
kappa = 1.15    ;                               % induced power factor
C_d0 = 0.008     ; % profile drag coefficient of the blade
[alpha, ~] = RC_AoAandThrust(V_cr_man, MTOW);
alpha_TPP = alpha     ;  % angle of attack in cruise [deg]
[~ , D_q_tot_x] = parasite_drag() ;
f = D_q_tot_x        ;                            % equivalent area estimated from reference A/C [m2]
A_rotor = R_prop_big^2 * pi * N_prop_big + R_prop_small^2 * pi * N_prop_small   ;        % rotor area in [m2]
mu = (V_cr_man * cos(deg2rad(alpha_TPP))) / (omega_prop * R_prop_big)   ; % advance ratio [~]
% Calculate the dimensionalizing factor
P_fact = rho * A_rotor * (R_prop_big*omega_prop)^3   ;
%    % Caculate the thrust coefficient
C_T = (MTOW * g / cos(deg2rad(alpha_TPP)) ) / (rho * (R_prop_big * omega_prop)^2 * A_rotor)   ;

C_P0 = sigma * C_d0 * (1 + (K * mu^2)) / 8     ;
P0 = C_P0 * P_fact       ;


% it is assumed that mu >> lambda here
C_Pi = kappa * C_T^2 / (2 * mu)   ; %Induced power coefficient [-]
Pi = C_Pi * P_fact    ;


C_Pp = 0.5 * mu^3 * (f/A_rotor) ;%Parisative power coefficient [-]
Pp = C_Pp * P_fact    ;
    



Preq_cruise = P0 + Pi + Pp   ; %Total power from components [W]
cruisepower = round((Preq_cruise/1000),2);

end