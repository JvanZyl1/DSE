function [L] = tipvalidation(MTOW)
    inputs;
    
    if MTOW <= 0
        error('invalid value of MTOW')
    end

    %define the airfoil polars:
    addpath("Excel\");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
    %plot(alpha,polyval(Cl_polar,alpha))
    
    rho_emp = 0.002377;  % slug/ft^3

    V_cr = 1.68780986 * 110;
    tilt = 6 / 180 * pi;

    V_TO_emp = V_TO * 3.2808399;  % ft/s
    V_z_list = V_TO_emp;
    %V_z_list = V_cr * sin(tilt);
    
    R_emp = 13.2;
    C_emp = 0.56;
    B_prop = 5;
    R_hub_emp = 0.2 * R_emp;

    nr_stations = 100;
    dr = (R_emp-R_hub_emp) / nr_stations;  % ft
    sos_emp = 1125.32808; % ft/s
    fprintf('dr = %f \n', dr)
    
    T_TO = 3000 * 0.45359237 * g * 0.2248089431 * 1.1;
    T_cr = 0.6 * T_TO;
    T_list = T_TO;
    %T_list = T_cr;
    RPM_list = 1;
    rpm = 680 / R_emp / (2*pi) * 60;
    lin_twist_list = -9;
    fprintf('rpm = %f \n', rpm)

    sigma = 0.068;  % solidity ratio
    j = 1;
    %RPM_list = 600:100:6000;
    for T=T_list
        i=1;
        V_i_emp = sqrt(T/(2*rho_emp*pi*R_emp^2)); %induced velocity at the rotor
        for lin_twist=lin_twist_list

            for RPM=RPM_list
                r = R_hub_emp;
                omega = 680 / R_emp;

                C_T_sigma = T_cr / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);  % Blade pitch optimized for cruise
                theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2));  % deg
                theta_tip = 14.5 + lin_twist;

                V_z = V_z_list(j);
                L_blade = 0;
                k = 1;
                for station=1:nr_stations
                    r = r + dr;
                    V_blade = omega * r;
                    V = sqrt((V_z+V_i_emp)^2 + (V_blade)^2);
                    
                    lin_twist_eff = 0.8 * lin_twist;
                    theta_local_deg = theta_tip - (1-(r-R_hub_emp)/(R_emp-R_hub_emp)) * lin_twist_eff;  % deg
                    theta_local = theta_local_deg * pi / 180;

                    alpha = theta_local - atan((V_z+V_i_emp)/(V_blade));
                    alpha_deg = alpha * 180 / pi;
                    Cl = polyval(Cl_polar,alpha_deg);
                    if alpha_deg < alpha_min || alpha_deg>alpha_stall
                        Cl = 0;
                    end
                    dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
                    dL_z = dL * cos(alpha);
                    L_blade = L_blade + dL_z;

                    fprintf('theta_local_deg %f, alpha_deg %f, dL_z = %f, V = %f, V_blade = %f, r = %f, omega = %f  \n', theta_local_deg, alpha_deg, dL_z, V, V_blade, r, omega)

                    k = k + 1;
                end
                L = L_blade * B_prop;
                fprintf('L = %f, T = %f \n', L, T)
                
                i = i + 1;

            end
            
        end
        j = j + 1;
    end

end

