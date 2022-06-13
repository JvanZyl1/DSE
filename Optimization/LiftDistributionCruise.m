function [RPM_opt] = LiftDistributionCruise(MTOW)
% SENSITIVITY ANALYSIS: change the following parameters
    % Thrust
    % Velocity
    %R_prop = 0.4;

    inputs;
    
    if MTOW <= 0
        error('invalid value of MTOW')
    end

    %define the airfoil polars:
    addpath("Excel\");

    fileName = 'xf-naca23012-il-1000000.csv';
    [alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
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
    %tilt_cr = 3 / 180 * pi;
    %V_cr  = 20;
    V_z_cr = V_cr * sin(tilt_cr) * 3.2808399;
    V_x_cr = V_cr * cos(tilt_cr) * 3.2808399;
    fprintf('V_z_cr, V_x_cr = %f, %f \n', V_z_cr, V_x_cr)
    
    % Thrusts required for flight modes
    T_TO = 1.1 * MTOW * g / N_prop * 0.2248089431;  % lb
    T_cr = T_TO * 0.6; %cos(tilt_cr); % T_cr * 0.2248089431; %%%%%%%%%%%%% TBD  % lb
    T = T_cr;
    % Setting variables for iteration loops
    %P_list = [];
    %theta_tip_opt_list = zeros(1, numel(T_list));
    %lin_twist_list = -10:-1:-90;  % deg
    lin_twist = -20;

    alpha_deg_list = zeros(1, nr_stations);

    V_i_emp = sqrt(T/(2*rho_emp*pi*R_emp^2)); %induced velocity at the rotor
    theta_tip = 10;
    L_sum = 0;
    %P = 0;
    k = 1;
    rot_angles = 10:10:360;
    dldr = zeros(numel(rot_angles), nr_stations);
    RPM_opt = 1000000;
    RPM_list = 500:100:1500;
    RPM_list = 900;
    for RPM=RPM_list
        omega = RPM * 2 * pi / 60;
        i =  1;
        for rot_deg=rot_angles
            rot_rad = rot_deg * pi / 180;
            L_blade = 0;
            r = R_hub_emp;
            r_list = [];
            for station=1:nr_stations
                r = r + dr;
                V_blade = omega * r;
                V = sqrt((V_z_cr+V_i_emp)^2 + (V_blade+cos(rot_rad) * V_x_cr)^2);
                %fprintf('velocities: %f %f %f %f \n', V_z_cr, V_i_emp, V_blade, V_x_cr)
    
                % Ideal twist
                % theta_local = theta_tip / (r / R_emp) * pi/180;  
    
                % Linear twist
                theta_local_deg = theta_tip - (1-(r-R_hub_emp)/(R_emp-R_hub_emp)) * lin_twist;  % deg
                %fprintf('theta tip = %f, r = %f, R_hub_emp = %f, R_emp = %f \n', theta_tip, r, R_hub_emp, R_emp)
                theta_local = theta_local_deg * pi / 180;
                %fprintf('thetalocal = %f deg', theta_local_deg)
    
                %fprintf('incoming airflow = %f \n', atan((V_TO_emp+V_i_emp)/V_blade)*180/pi)
                alpha = theta_local - atan((V_z_cr+V_i_emp)/(V_blade+cos(rot_rad) * V_x_cr));
                alpha_deg = alpha * 180 / pi;
                fprintf('V_blade = %f, V_x_cr = %f, alpha deg = %f at rot_deg = %f  \n', V_blade, V_x_cr*cos(rot_rad), alpha_deg, rot_deg)
                Cl = polyval(Cl_polar,alpha_deg);
                if alpha_deg < alpha_min || alpha_deg>alpha_stall
                    Cl = 0;
                end
                dL = 0.5 * Cl * rho_emp * V * V * C_emp * dr;
                dL_z = dL * cos(alpha);
                L_blade = L_blade + dL_z;
                %fprintf('L_blade = %f \n', L_blade)

                dldr(i, station) = dldr(i, station) + dL_z * dr;
                r_list(end+1) = r;
            end
            L_sum = L_sum + L_blade * B_prop;
            %fprintf('L_sum = %f at rot_deg = %f \n', L_sum, rot_deg)
            i = i + 1;
    
        end
        L = L_sum / numel(rot_angles);
        dldr = dldr / numel(rot_angles);
        fprintf('L, T = %f, %f \n', L, T)
        if L>T && RPM < RPM_opt
            RPM_opt = RPM;
            fprintf('RPM_opt for cruise = %f \n', RPM_opt)
            break
        end
    end
    r_list = r_list / 3.2808399;
    dldr_list = dldr / 0.2248089431;
    fprintf('sizes')
    disp([size(r_list), size(rot_angles), size(dldr_list)])
    fig1 = figure(1);
    surf(r_list,rot_angles,dldr_list)
    xlabel('r [m]');
    ylabel('$\Omega$ [RPM]','Interpreter','latex');
    zlabel('$\Delta L / \Delta R$ [N/m]','Interpreter','latex');
    %savefig(fig1,'Figures/ControlPropellerFig3')
end

