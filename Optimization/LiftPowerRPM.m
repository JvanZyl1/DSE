function [] = LiftPowerRPM(MTOW, RPM_list)
    inputs;
    %define the airfoil polars:
    addpath("Excel");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
    plot(alpha,polyval(Cl_polar,alpha))

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
    T_cr = T_TO * (2/3); %%%%%%%%%%%%% TBD
    T_em = 1.5 * T_TO; %%%%%%%%%%%%% TBD
    i=1;
    j = 1;
    T_list = [T_TO, T_cr, T_em];
    L_list = zeros(1, numel(RPM_list));
    RPM_opt_list = zeros(1, numel(T_list));
    for T=T_list
        for RPM=RPM_list
            omega = RPM * 2 * pi / 60;
            fprintf('Inputs: T = %f, rho = %f, sigma = %f, R = %f, omega = %f\n', T, rho, sigma, R_prop, omega)
            C_T_sigma = T / (rho * sigma * pi*R_prop^2 * (omega * R_prop)^2);
            theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2));% * (pi/180);
            fprintf('C_T_sigma = %f, theta_tip = %f\n', C_T_sigma, theta_tip)
            r = 0;
            for station=1:nr_stations-1
                r = r + dr;
                %Cl = Cl_dist(station);
                V_blade = omega * station * dr;
                M_blade = V_blade / 343;
                V = sqrt((V_TO+V_i)^2 + V_blade^2);
    
                theta_local = theta_tip / (r / R);
                alpha = theta_local - atan(V_TO/V_blade);
                Cl = polyval(Cl_polar,alpha);
    
                dL = 0.5 * Cl * rho * V * V * C_prop * dr;
                L_blade = L_blade + dL;
    
                %fprintf('Local velocity = %f [m/s] \n Local Mach number = %f []\n', V_blade, M_blade)
            end
            L = L_blade * B_prop;
            L_list(i) = L;
            if L>T
                RPM_opt = RPM;
                break
            end
            i = i + 1;
        end
        RPM_opt_list(j) = RPM_opt;
        j = j + 1;
    end
    fprintf('RPM required for take-off = %f \n RPM required for cruise = %f \n RPM required for emergency = %f \n', RPM_opt_list(1), RPM_opt_list(2), RPM_opt_list(3))
end

