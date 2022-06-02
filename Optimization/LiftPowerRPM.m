function [RPM_opt_list] = LiftPowerRPM(MTOW, RPM_list)
    inputs;
    %define the airfoil polars:
    addpath("Excel\");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
    plot(alpha,polyval(Cl_polar,alpha))
    
    % For parametric calculations with emperical units
    R_emp = 3.2808399 * R_prop;  % ft
    C_emp = 3.2808399 * C_prop;  % ft
    rho_emp = 0.002377;  % slug/ft^3

    nr_stations = 100;
    V_i = 0.5;
    %Cl_root_tip = [1.5, 0.5];
    
    dr = R_emp / nr_stations;  % ft
    
    %dCl = (Cl_root_tip(1) - Cl_root_tip(2)) / (nr_stations-1);
    %Cl_dist = Cl_root_tip(1):-dCl:Cl_root_tip(2)+dCl;


    %dCl = (Cl_root_tip(1) - Cl_root_tip(2)) / (nr_stations-1);
    %Cl_dist = Cl_root_tip(1):-dCl:Cl_root_tip(2)+dCl;

    sigma = (R_prop * C_prop * B_prop) / (pi * R_prop^2);  % solidity ratio
    sos_emp = 1125.32808;
    V_TO_emp = V_TO * 3.2808399;  % ft/s
    V_i_emp = V_i * 3.2808399;  % ft/s
    L_blade = 0;
    T_TO = 1.1 * 1.5 * MTOW * g / N_prop;
    T_cr = T_TO * (2/3); %%%%%%%%%%%%% TBD
    T_em = 1.5 * T_TO; %%%%%%%%%%%%% TBD
    i=1;
    j = 1;
    T_list = [T_TO, T_cr, T_em] * 	0.2248089431;  % lb
    L_list = zeros(1, numel(RPM_list));
    RPM_opt_list = zeros(1, numel(T_list));
    for T=T_list
        for RPM=RPM_list
            omega = RPM * 2 * pi / 60;
            C_T_sigma = T / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);
            disp(C_T_sigma)
            theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2)) * (pi/180);  % rad
            r = 0;
            for station=1:nr_stations-1
                r = r + dr;
                %Cl = Cl_dist(station);
                V_blade = omega * station * dr;
                M_blade = V_blade / sos_emp;
                V = sqrt((V_TO_emp+V_i_emp)^2 + V_blade^2);
    
                theta_local = theta_tip / (r / R_emp);
                alpha = theta_local - atan(V_TO_emp/V_blade);
                alpha_deg = alpha * 180 / pi;
                Cl = polyval(Cl_polar,alpha_deg);
                if Cl < alpha_min || Cl>alpha_stall
                    Cl = 0;
                end
                fprintf('At alpha = %f [deg], Cl = %f\n', alpha_deg, Cl)
    
                dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
                L_blade = L_blade + dL;
    
                %fprintf('Local velocity = %f [m/s] \n Local Mach number = %f []\n', V_blade, M_blade)
            end
            L = L_blade * B_prop;
            L_list(i) = L;
            fprintf(['Inputs: T = %f, rho = %f, sigma = %f, R = %f, omega = %f\n' ...
                'C_T_sigma = %f, V_tip = %f, alpha = %f \n'], T, rho_emp, sigma, R_emp, omega, C_T_sigma, V, alpha)
            fprintf('For RPM = %f, the lift produced per propeller is %f \n', RPM, L)
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

