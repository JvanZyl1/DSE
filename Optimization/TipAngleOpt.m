function [RPM_opt_list, lin_twist, T_list,V_i_emp] = TipAngleOpt(MTOW)
    inputs;
    

    % SENSITIVITY ANALYSIS: change the following parameters
    % Thrust
    % Velocity
    %R_prop = 0.4;
    
    if MTOW <= 0
        error('invalid value of MTOW')
    end

    %define the airfoil polars:
    addpath("Excel\");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, ~] = ReadPolar(fileName);
    %plot(alpha,polyval(Cl_polar,alpha))
    
    % For parametric calculations with emperical units
    R_emp = 3.2808399 * R_prop;  % ft
    C_emp = 3.2808399 * C_prop;  % ft
    R_hub_emp = 3.2808399 * (R_hub + 0.0875);  % ft, hub radius + transition to actual airfoil part
    rho_emp = 0.002377;  % slug/ft^3

    nr_stations = 20;
    dr = (R_emp-R_hub_emp) / nr_stations;  % ft
    sos_emp = 1125.32808; % ft/s

    [tilt_cr, ~] = RC_AoAandThrust(V_cr, MTOW);
    %tilt_cr = 6 / 180 * pi;
    V_z_cr = V_cr * sin(tilt_cr) * 3.2808399;
    fprintf('tilt angle = %f, V_z = %f \n', tilt_cr, V_z_cr)
    V_TO_emp = V_TO * 3.2808399;  % ft/s
    V_L_emp = -3 * 3.2808399;  % ft/s
    V_z_list = 0.5 * [V_z_cr, V_TO_emp, V_L_emp, 0];
    %V_z_list = [V_TO_emp, V_L_emp, V_z_cr, 0];
    
    % Thrusts required for flight modes
    T_TO = 1.1 * MTOW * g / N_prop * 0.2248089431;  % lb
    T_L = T_TO;
    T_cr = T_TO * 0.8; %cos(tilt_cr); % T_cr * 0.2248089431; %%%%%%%%%%%%% TBD  % lb
    T_em = 38500 * 0.2248089431; %1.5 * T_TO; %%%%%%%%%%%%% TBD  % lb

    T_list = [T_cr, T_TO, T_L, T_em];  % lb
    T_list = T_em;  % lb
    sigma = (R_emp * C_emp * B_prop) / (pi * R_emp^2);  % solidity ratio

    % Setting variables for iteration loops
    j = 1;
    RPM_list = 100:100:6000;
    RPM_opt_list = [];
    %L_list = [];
    M_tip_opt_list = [];
    %theta_tip_opt_list = zeros(1, numel(T_list));
    lin_twist_list = -10:-1:-90;  % deg
    %lin_twist_list = -38;

    alpha_deg_list = zeros(1, nr_stations);
    for T=T_list
        i=1;
        V_i_emp = sqrt(T/(2*rho_emp*pi*R_emp^2)); %induced velocity at the rotor
        %fprintf('T = %f', T)
        if j>1
            lin_twist_list = lin_twist_opt;  % Taking optimum twist for cruise
            %theta_start = theta_start_opt;
            theta_tip = theta_tip_opt;
        end

        RPM_opt = RPM_list(end);
        for lin_twist=lin_twist_list

            for RPM=RPM_list
                r = R_hub_emp;
                omega = RPM * 2 * pi / 60;
                if j == 1
                    C_T_sigma = T_cr / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);  % Blade pitch optimized for cruise
                    theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2));  % deg
                end
                %theta_tip = 10;
                V_z = V_z_list(j);
                L_blade = 0;
                k = 1;
                for station=1:nr_stations                
                    r = r + dr;
                    V_blade = omega * r;
                    V = sqrt((V_z+V_i_emp)^2 + V_blade^2);
    
                    % Ideal twist
                    % theta_local = theta_tip / (r / R_emp) * pi/180;  
    
                    % Linear twist
                    theta_local_deg = theta_tip - (1-(r-R_hub_emp)/(R_emp-R_hub_emp)) * lin_twist;  % deg
                    theta_local = theta_local_deg * pi / 180;
                    %fprintf('thetalocal = %f deg', theta_local)

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
                    %fprintf('dL = %f \n', dL_z)
                end
                L = L_blade * B_prop;
                %fprintf('L = %f \n', L)
                if L>T && RPM < RPM_opt
                    RPM_opt = RPM;
                    %RPM_opt_list(end+1) = RPM;
                    M_tip_opt =  V / sos_emp;
                    %theta_start_opt=theta_start;
                    lin_twist_opt = lin_twist;
                    %fprintf('For j = %i, RPM_opt = %f for twist = %f.\n', j, RPM, lin_twist)
                    %theta_tip_opt = theta_local_deg;
                    % fprintf('lin_twist = %f, L = %f, T = %f, RPM = %f \n', lin_twist, L, T, RPM)
                    break
                
                end
                i = i + 1;

            end
            
        end
        %theta_start_list(end+1) = theta_start_opt;
        RPM_opt_list(end+1) = RPM_opt;
        lin_twist_list = lin_twist;
        theta_tip_opt = theta_tip;
        M_tip_opt_list(end+1) = M_tip_opt;
        j = j + 1;

        %fprintf('optimal lin twist = %f , theta_tip = %f, giving RPM = %f \n', lin_twist_opt, theta_tip, RPM_opt)
        
        %fprintf('optimal lin twist = %f with theta_start = %f, giving RPM = %f \n', lin_twist_opt, theta_start_opt, RPM_opt)

        %RPM_opt_list(j) = RPM_opt;
        %M_tip_opt_list(j) = M_tip_opt;
        %theta_tip_opt_list(j) = theta_tip_opt;
        %fprintf('For mode %i: lin_twist = \n', j)
        %disp(lin_twist_list)
        %fprintf('and RPM_list = \n')
        %disp(RPM_opt_list)
        %j = j + 1;
        %fprintf('theta_tip = %f \n', theta_tip_opt)
    end
    fprintf(['Optimal linear twist for cruise conditions = %f with tip pitch angle = %f\n' ...
        'RPM required for cruise = %f \n RPM required for take-off = %f \n RPM required for landing = %f \n RPM required for emergency = %f \n'], lin_twist_opt(end), theta_tip, RPM_opt_list)

    disp(M_tip_opt_list)
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