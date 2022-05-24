function [W_bat, E_total] = BatteryMassViaDrag(V_cr_man,MTOW)

inputs;
%V_cr_man = V_cr;
PowerReq(MTOW,V_cr_man);
PowerViaDrag(V_cr_man, MTOW);
[~,P_TOL,P_cont] = PowerReq(MTOW,V_cr_man);
[P_cruise_KW,~,~,~] = PowerViaDrag(V_cr_man, MTOW);
P_cruise = P_cruise_KW*1000;
eta_E = eta_E * 1.08^(yop-2022);
t_CR = (R + R_div) / (V_cr_man)  ;   % Calculate time in cruise + diversion
t_TO = (h_TO / V_TO) * 2   ;                  % Calculate the time spent in vertical flight
t_cont = t_TO  ;
% Energy required for flight phases
E_CR = t_CR * P_cruise ;
E_TO = t_TO * P_TOL  ;
E_cont = t_cont * P_cont  ;
E_total = (E_TO + E_CR + E_cont) / 3600  ;               % total energy needed in [Wh]
W_bat = (E_total / eta_E) / nu_discharge  ;
end