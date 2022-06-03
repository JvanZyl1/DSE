function [RPM_opt_list, lin_twist] = LiftPowerRPM(MTOW)
    inputs;


    %%%%%%%%%% TODO %%%%%%%%%%
    % Enlargen hub to get rid of inaccurate Cl due to ideal twist
    % Set a constant twist for all flight cases
    % Output rotor geometry

    %define the airfoil polars:
    addpath("Excel\");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, ~] = ReadPolar(fileName);
    plot(alpha,polyval(Cl_polar,alpha))
    
    % For parametric calculations with emperical units
    R_emp = 3.2808399 * R_prop;  % ft
    C_emp = 3.2808399 * C_prop;  % ft
    R_hub_emp = 3.2808399 * (R_hub + 0.0875);  % ft, hub radius + transition to actual airfoil part
    rho_emp = 0.002377;  % slug/ft^3

    nr_stations = 20;
    dr = (R_emp-R_hub_emp) / nr_stations;  % ft
    sos_emp = 1125.32808; % ft/s

    [tilt_cr, ~] = RC_AoAandThrust(V_cr, MTOW);
    V_z_cr = V_cr * sin(tilt_cr) * 3.2808399;
    fprintf('tilt angle = %f, V_z = %f \n', tilt_cr, V_z_cr)
    V_TO_emp = V_TO * 3.2808399;  % ft/s
    %V_z_list = [V_z_cr, V_TO_emp, 0];
    V_z_list = [V_TO_emp, V_z_cr, 0];
    
    % Thrusts required for flight modes
    T_TO = 1.1 * 1.5 * MTOW * g / N_prop * 0.2248089431;  % lb
    T_cr = T_TO * (2/3); %%%%%%%%%%%%% TBD  % lb
    T_em = 1.5 * T_TO; %%%%%%%%%%%%% TBD  % lb

    %T_list = [T_cr, T_TO, T_em];  % lb
    T_list = [T_TO, T_cr, T_em];  % lb
    %sigma = (R_emp * C_emp * B_prop) / (pi * R_emp^2);  % solidity ratio

    % Setting variables for iteration loops
    j = 1;
    RPM_list = 500:100:5000;
    %L_list = [];
    RPM_opt_list = zeros(1, numel(T_list));
    M_tip_opt_list = zeros(1, numel(T_list));
    theta_tip_opt_list = zeros(1, numel(T_list));
    lin_twist_list = -5:-1:-45;  % deg
    alpha_deg_list = zeros(1, nr_stations);
    for T=T_list
        i=1;
        V_i_emp = sqrt(T/(2*rho_emp*pi*R_emp^2)); %induced velocity at the rotor
        RPM_opt_twist = RPM_list(end);
        %fprintf('T = %f', T)
        if j>1
            lin_twist_list = lin_twist_opt;  % Taking optimum twist for cruise
            theta_start = theta_start_opt;
        end

        for lin_twist=lin_twist_list
            %fprintf('lin_twist = %f, T = %f\n', lin_twist, T)
            %col_twist = 1.5 * theta_tip - 0.75 * lin_twist;  % deg

            for RPM=RPM_list
                r = R_hub_emp;
                omega = RPM * 2 * pi / 60;
                %C_T_sigma = T_cr / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);  % Blade pitch optimized for cruise
                %theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2));  % deg
                V_z = V_z_list(j);
                if j == 1
                    theta_start = -1.2 + atan((V_z+V_i_emp)/(omega * r))*180/pi;  % deg
                end
                L_blade = 0;
                k = 1;
                for station=1:nr_stations                
                    r = r + dr;
                    V_blade = omega * r;
                    V = sqrt((V_z+V_i_emp)^2 + V_blade^2);
                    M_tip = V / sos_emp;
    
                    % Ideal twist
                    % theta_local = theta_tip / (r / R_emp) * pi/180;  
    
                    % Linear twist
                    theta_local_deg = theta_start + (r-R_hub_emp)/(R_emp-R_hub_emp) * lin_twist;  % deg
                    theta_local = theta_local_deg * pi / 180;

                    %fprintf('incoming airflow = %f \n', atan((V_TO_emp+V_i_emp)/V_blade)*180/pi)
                    alpha = theta_local - atan((V_z+V_i_emp)/V_blade);
                    alpha_deg = alpha * 180 / pi;
                    Cl = polyval(Cl_polar,alpha_deg);
                    if alpha_deg < alpha_min || alpha_deg>alpha_stall
                        Cl = 0;
                    end
                    dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
                    dL_z = dL * cos(alpha);
                    L_blade = L_blade + dL_z;
                    %fprintf('r = %f \n', r)
                    if j>1
                        %fprintf('theta = %f at r = %f \n', theta_local_deg, r)
                    end
                    alpha_deg_list(k) = alpha_deg;
                    k = k + 1;
                end
                L = L_blade * B_prop;
                i = i + 1;
                if L>T && RPM < RPM_opt_twist
                    RPM_opt_twist = RPM;
                    M_tip_opt = M_tip;
                    lin_twist_opt = lin_twist;
                    theta_start_opt=theta_start;
                    %fprintf('RPM_opt = %f for twist = %f. Local Mach number at tip = %f\n', RPM, lin_twist,M_tip)
                    theta_tip_opt = theta_local_deg;
                    if j == 1
                        disp(alpha_deg_list)
                    end
                end

            end
        end
        RPM_opt_list(j) = RPM_opt_twist;
        M_tip_opt_list(j) = M_tip_opt;
        theta_tip_opt_list(j) = theta_tip_opt;
        j = j + 1;
        fprintf('theta_tip = %f \n', theta_tip_opt)
    end
    fprintf(['Optimal linear twist for cruise conditions = %f with pitch at hub = %f\n' ...
        'RPM required for cruise = %f \n RPM required for take-off = %f \n RPM required for emergency = %f \n'], lin_twist_opt, theta_start, RPM_opt_list(1), RPM_opt_list(2), RPM_opt_list(3))
end



%V_blade_arr = omega * r_arr;
%             %disp(V_blade_arr)
%             M_tip = V_blade_arr(end) / sos_emp;
%             V = sqrt(ones(1, numel(r_arr))*(V_TO_emp+V_i_emp)^2 + V_blade_arr.^2);
% 
% 
%             %disp(atan((ones(1, numel(r_arr)) *(V_TO_emp+V_i_emp) ./ V_blade_arr)*180/pi))
%             %disp(atan(V_TO_emp+V_i_emp*180/pi))
% 
% 
%             theta_local_arr = theta_tip ./ (r_arr / R_emp);
%             disp(theta_local_arr)
%             alpha_arr = theta_local_arr - atan((ones(1, numel(r_arr)) *(V_TO_emp+V_i_emp) ./ V_blade_arr));
%             alpha_deg_arr = alpha_arr * 180 / pi;
%             %disp(alpha_deg_arr)
%             alpha_deg_arr = alpha_deg_arr(alpha_deg_arr<alpha_stall & alpha_deg_arr>alpha_min);
%             %disp(alpha_deg_arr)
%             %disp(alpha_deg_arr)
%             Cl_arr = polyval(Cl_polar,alpha_deg_arr);
% %                 for i=1:numel(Cl_arr)
% %                     if Cl_arr(i)<alpha_min || Cl_arr(i)>alpha_stall
% %                         Cl_arr(i) = 0;
% %                     end
% %                 end
%             V = V(alpha_deg_arr<alpha_stall & alpha_deg_arr>alpha_min);
%             %dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
%             L = sum(0.5 * Cl_arr .* V.^2  * rho_emp* dr * C_emp) * B_prop;
%             %disp(L)
%             %disp(V_blade_arr)