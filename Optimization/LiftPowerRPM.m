function [] = LiftPowerRPM(MTOW, RPM_list)
    inputs;

    nr_stations = 10;
    V_i = 0.5;
    %Cl_root_tip = [1.5, 0.5];
    
    dr = R_prop / nr_stations;
    
    %dCl = (Cl_root_tip(1) - Cl_root_tip(2)) / (nr_stations-1);
    %Cl_dist = Cl_root_tip(1):-dCl:Cl_root_tip(2)+dCl;


    %dCl = (Cl_root_tip(1) - Cl_root_tip(2)) / (nr_stations-1);
    %Cl_dist = Cl_root_tip(1):-dCl:Cl_root_tip(2)+dCl;

    sigma = (R_prop * C_prop * B_prop) / (pi * R_prop^2);  % solidity ratio
    
    L_blade = 0;
    T_TO = 1.1 * 1.5 * MTOW * g / N_prop;
    T_cr = L_TO * (2/3); %%%%%%%%%%%%% TBD
    T_em = 1.5 * L_TO; %%%%%%%%%%%%% TBD
    i=1;
    T_list = [T_TO, T_cr, T_em];
    L_list = zeros(1, numel(RPM_list));
    for T=T_list
        for RPM=RPM_list
            omega = RPM * 2 * pi / 60;
            C_T_sigma = T / (rho * sigma * A_disk * (omega * R_prop)^2);
            theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2)) * (2*pi/180);
            r = 0;
            for station=1:nr_stations-1
                r = r + dr;
                %Cl = Cl_dist(station);
                V_blade = omega * station * dr;
                M_blade = V_blade / 343;
                V = sqrt((V_TO+V_i)^2 + V_blade^2);
    
                theta_local = theta_tip / (r / R);
                alpha = theta_local - atan(V_TO/V_blade);
                Cl = Cl_slope * alpha;
    
                dL = 0.5 * Cl * rho * V * V * C_prop * dr;
                L_blade = L_blade + dL;
    
                fprintf('Local velocity = %f [m/s] \n Local Mach number = %f []\n', V_blade, M_blade)
            end
            L = L_blade * B_prop;
            L_list(i) = L;
            if L>T
                RPM_opt = RPM;
                break
            end
            i = i + 1;
        end
    end
    fprintf('RPM required for take-off = %f \n RPM required for cruise = %f \n RPM required for emergency = %f \n', RPM_TO, RPM_cr, RPM_em)
end

