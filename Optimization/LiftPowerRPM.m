function [RPM_opt_list, lin_twist] = LiftPowerRPM(MTOW, RPM_list)
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
    R_hub_emp = 3.2808399 * R_hub;  % ft
    rho_emp = 0.002377;  % slug/ft^3
    nr_stations = 10;
    dr = (R_emp-R_hub_emp) / nr_stations;  % ft
    sos_emp = 1125.32808; % ft/s
    V_TO_emp = V_TO * 3.2808399;  % ft/s
    
    % Thrusts required for flight modes
    T_TO = 1.1 * 1.5 * MTOW * g / N_prop * 0.2248089431;  % lb
    T_cr = T_TO * (2/3); %%%%%%%%%%%%% TBD  % lb
    T_em = 1.5 * T_TO; %%%%%%%%%%%%% TBD  % lb
    T_list = [T_cr, T_TO, T_em];  % lb

    %sigma = (R_emp * C_emp * B_prop) / (pi * R_emp^2);  % solidity ratio

    % Setting variables for iteration loops
    j = 1;
    RPM_list = 500:100:2000;
    L_list = [];
    RPM_opt_list = zeros(1, numel(T_list));
    lin_twist_list = -10:-1:-30;  % deg
    disp(lin_twist_list)
    for T=T_list
        i=1;
        V_i_emp = sqrt(T/(2*rho_emp*pi*R_emp^2)); %induced velocity at the rotor
        RPM_opt_twist = RPM_list(end);
        %fprintf('T = %f', T)
        if j>1
            lin_twist_list = lin_twist_opt;  % Taking optimum twist for cruise
        end
        for lin_twist=lin_twist_list
            fprintf('lin_twist = %f, T = %f\n', lin_twist, T)
            
            %col_twist = 1.5 * theta_tip - 0.75 * lin_twist;  % deg
            %fprintf('Tip pitch angle = %f and col_twist = %f \n',theta_tip, col_twist)

            for RPM=RPM_list
                r = R_hub_emp;
                omega = RPM * 2 * pi / 60;
                %C_T_sigma = T_cr / (rho_emp * sigma * pi*R_emp^2 * (omega * R_emp)^2);  % Blade pitch optimized for cruise
                %theta_tip = 57.3 * (4/Cl_slope*C_T_sigma + sqrt(sigma * C_T_sigma / 2));  % deg
                col_twist = -1.2 + atan((V_TO_emp+V_i_emp)/(omega * r))*180/pi;  % deg
                %fprintf('coltwist = %f \n', col_twist)
                L_blade = 0;
                %Cl_list = [];
                %k = 1;
                for station=1:nr_stations-1                
                    r = r + dr;
                    V_blade = omega * station * dr;
                    V = sqrt((V_TO_emp+V_i_emp)^2 + V_blade^2);
                    M_tip = V / sos_emp;
    
                    % Ideal twist
                    % theta_local = theta_tip / (r / R_emp) * pi/180;  
    
                    % Linear twist
                    theta_local_deg = col_twist + r/R_emp * lin_twist;  % deg
                    theta_local = theta_local_deg * pi / 180;
                    %fprintf('incoming airflow = %f \n', atan((V_TO_emp+V_i_emp)/V_blade)*180/pi)
                    alpha = theta_local - atan((V_TO_emp+V_i_emp)/V_blade);
                    alpha_deg = alpha * 180 / pi;
                    Cl = polyval(Cl_polar,alpha_deg);
                    if alpha_deg < alpha_min || alpha_deg>alpha_stall
                        Cl = 0;
                    end
                    %fprintf('RPM = %f, AoA = %f, Cl = %f\n V_blade = %f and V_z = %f with local pitch = %f \n', RPM, alpha_deg, Cl, V_blade, V_TO_emp+V_i_emp, theta_local*180/pi)
                    %fprintf('At alpha = %f [deg] (pitch = %f, Cl = %f\n', alpha_deg, theta_local*180/pi, Cl)
                    %Cl_list(k) = Cl;
                    %disp(Cl_list)
                    dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
                    dL_z = dL * cos(alpha);
                    %fprintf('dL = %f, dL_z = %f, alpha_deg = %f \n', dL, dL_z, alpha_deg)
                    L_blade = L_blade + dL_z;
                    %k = k + 1;
                end
                %fprintf('V_i = %f \n, L = %f', V_i_emp, L)
                L = L_blade * B_prop;
                %L_list(i) = L;
                %disp(L_list)
                i = i + 1;
                %fprintf(['L = %f [N], T = %f, rho = %f, sigma = %f, R = %f, omega = %f\n' ...
                %    'C_T_sigma = %f, V_tip = %f, alpha = %f \n'], L, T, rho_emp, sigma, R_emp, omega, C_T_sigma, V, alpha)
                %fprintf('For RPM = %f, the lift produced per propeller is %f \n', RPM, L)
                %fprintf('WHATS WROOONGG, alpha_deg = %f, V = %f\n', alpha_deg, V)
                if L>T && RPM < RPM_opt_twist
                    RPM_opt_twist = RPM;
                    lin_twist_opt = lin_twist;
                    fprintf('RPM_opt = %f for twist = %f. Local Mach number at tip = %f\n', RPM, lin_twist,M_tip)
                end
            end
        end
        RPM_opt_list(j) = RPM_opt_twist;
        %lin_twist_opt_list(j) = lin_twist_opt;
        j = j + 1;
    end
    fprintf('RPM required for take-off = %f \n RPM required for cruise = %f \n RPM required for emergency = %f \n', RPM_opt_list(1), RPM_opt_list(2), RPM_opt_list(3))
    %disp(lin_twist_opt_list)
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