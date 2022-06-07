function [W_bat, E_total, V_bat] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont)
    inputs;
    % eta_E = eta_E * 1.08^(yop-2022);   % Fulvio recommended NOT to use this
    t_cr = R / V_cr  ;   % Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2   ;   % Calculate the time spent in vertical flight
    t_cont = t_TO  ;  % Control propulsion time is overestimated

    % Energy required for flight phases, redundancy factor is taken out of
    % the battery sizing
    E_cr = t_cr * P_cruise * redundancy_factor ;
    E_TO = t_TO * P_TOL * redundancy_factor  ;
    E_cont = t_cont * P_cont  ;
    E_total = (E_TO + E_cr + E_cont) / 3600  ;               % total energy needed in [Wh]
    %W_bat = (E_total / nu_discharge ) / eta_E  ;

    %new battery weight, based on max P_req
    N_cells_series = ceil(Voltage/Cell_volt);    %voltage assumed a priori
    Amp_req = P_TOL/Voltage;                     
    N_cells_para = ceil(Amp_req/Cell_amp);
    N_cells = N_cells_para*N_cells_series;       
    W_bat = N_cells * CellToPack * Cell_mass;
    Capacity = N_cells * Cell_capa;
    V_bat = Capacity / vol_dens;  % https://insideevs.com/news/581729/volumetric-energy-density-ev-batteries-growth/
    Cell_costs = N_cells * Cell_price;

    E_div = R_div / V_cr;
    E_red = E_total * (1/nu_discharge - 1);
    if E_div > E_red
        E_total_old = E_total;
        E_total = E_div/(1 - nu_discharge);
        fprintf('The required divergence range is not compatible with the redundant energy at a DoD of %f.\nIf we scale the required energy up to make this happen, we have %f [Wh] of unnecessary energy.\n', nu_discharge, (E_total-E_total_old))
    end
    if Capacity < E_total
        disp('INSUFFICIENT BATTERY CAPACITY \n')
    end
    DoD_req = E_total/Capacity;
    fprintf('cells in series:%f ,cells in parallel:%f , total nr of cells:%f \n',N_cells_series,N_cells_para,N_cells)
    fprintf('energy required is %f [Wh] \n',E_total)
    fprintf('Battery capacity: %f [Wh] \n',Capacity)
    fprintf('Required DoD is: %f \n',DoD_req)
    fprintf('Battery cost: %f [$] \n',round(Cell_costs,1))

end