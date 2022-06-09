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
    E_div = R_div / V_cr;
    E_red = E_total * (1/nu_discharge - 1);

    N_cells_series = ceil(Voltage/Cell_volt);    %voltage assumed a priori

    %Cruise Battery
    Amp_req_cruise = P_cruise/Voltage;                     
    N_cells_para_cruise = ceil(Amp_req_cruise/Cell_amp);
    N_cells_cruise = N_cells_para_cruise*N_cells_series;
    Capacity_cruise = N_cells_cruise * Cell_capa;
    
    %W_bat = N_cells * CellToPack * Cell_mass;
    %V_bat = Capacity_cruise / vol_dens;  % https://insideevs.com/news/581729/volumetric-energy-density-ev-batteries-growth/
    %Cell_costs = N_cells * Cell_price;

    Amp_req_TO = P_TOL/Voltage;                     
    N_cells_para_TO = ceil(Amp_req_TO/TOCell_amp);   %%%%
    N_cells_TO = N_cells_para_TO*N_cells_series;
    Capacity_TO = N_cells_TO * TOCell_capa;      %%%%

    
    W_bat = (N_cells_TO*TOCell_mass + N_cells_cruise*Cell_mass)*CellToPack;
    Capacity_total = Capacity_cruise+Capacity_TO;
    V_bat = Capacity_total / vol_dens;  % https://insideevs.com/news/581729/volumetric-energy-density-ev-batteries-growth/
    
    if E_div > E_red
        E_total_old = E_total;
        E_total = E_div/(1 - nu_discharge);
        fprintf('The required divergence range is not compatible with the redundant energy at a DoD of %f.\nIf we scale the required energy up to make this happen, we have %f [Wh] of unnecessary energy.\n', nu_discharge, (E_total-E_total_old))
    end

    if Capacity_cruise < (E_cr + E_cont)/3600
        disp('INSUFFICIENT BATTERY CAPACITY CRUISE \n')
    end
    
    if Capacity_TO < (E_TO + E_cont)/3600
        disp('INSUFFICIENT BATTERY CAPACITY TAKEOFF \n')
    end
    DoD_req = E_total/Capacity_cruise;
    fprintf('Capa cruise: %f [Wh], E_cruise %f [Wh], DoD cruise %f \n',Capacity_cruise,(E_cr/3600),(E_cr/3600)/Capacity_cruise)
    fprintf('cells in series:%f ,cells in parallel:%f , total nr of cells:%f \n',N_cells_series,N_cells_para_cruise,N_cells_cruise)
    fprintf('Capa takeoff %f [Wh], E_TO %f [Wh], DoD takeoff %f \n',Capacity_TO,(E_TO/3600),(E_TO/3600)/Capacity_TO)
    fprintf('cells in series:%f ,cells in parallel:%f , total nr of cells:%f \n',N_cells_series,N_cells_para_TO,N_cells_TO)
    fprintf('CruiseBatWeight: %f [kg], TOBatWeight: %f [kg] \n',(N_cells_cruise*Cell_mass*CellToPack),(N_cells_TO*TOCell_mass*CellToPack))
    fprintf('E_tot=%f, Capa=%f, DoD is %f \n',E_total,Capacity_total,(E_total/Capacity_total))
    %fprintf('energy required is %f [Wh] \n',E_total)
    %fprintf('Battery Capacity: %f [Wh] \n',Capacity_cruise)
    %fprintf('Required DoD is: %f \n',DoD_req)
    %fprintf('Battery cost: %f [$] \n',round(Cell_costs,1))

end