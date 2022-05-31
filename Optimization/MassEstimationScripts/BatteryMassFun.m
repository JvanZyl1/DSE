function [W_bat, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont)
    inputs;
    % eta_E = eta_E * 1.08^(yop-2022);   % Fulvio recommended NOT to use this
    t_cr = R / V_cr  ;   % Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2   ;                  % Calculate the time spent in vertical flight
    t_cont = t_TO  ;
    % Energy required for flight phases
    E_cr = t_cr * P_cruise * redundancy_factor ;
    E_TO = t_TO * P_TOL * redundancy_factor  ;
    E_cont = t_cont * P_cont  ;
    E_total = (E_TO + E_cr + E_cont) / 3600  ;               % total energy needed in [Wh]
    W_bat = (E_total / nu_discharge ) / eta_E  ;
    V_bat = (E_total / nu_discharge) / vol_dens;  % https://insideevs.com/news/581729/volumetric-energy-density-ev-batteries-growth/
    
    E_div = R_div / V_cr;
    E_red = E_total * (1/nu_discharge - 1);
    if E_div > E_red
        E_total_old = E_total;
        E_total = E_div/(1 - nu_discharge);
        fprintf('The required divergence range is not compatible with the redundant energy at a DoD of %f.\nIf we scale the required energy up to make this happen, we have %f [Wh] of unnecessary energy.\n', nu_discharge, (E_total-E_total_old))
    end

end