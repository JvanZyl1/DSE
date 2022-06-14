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
    [~, Cl_polar, ~] = ReadPolar(fileName);
    
    % Convert blade dimensions to imperial units
    R_imp = 3.2808399 * R_prop;  % ft
    C_imp = 3.2808399 * C_prop;  % ft
    R_hub_imp = 3.2808399 * (R_hub + 0.0875);  % ft, hub radius + transition to actual airfoil part
    rho_imp = 0.002377;  % slug/ft^3
    
    % Define sections of blade for blade element theory
    nr_stations = 20;
    dr = (R_imp-R_hub_imp) / nr_stations;  % ft

    % Speed of sound in ft/s for calculations of blade tip Mach number
    sos_imp = 1125.32808; % ft/s
    
    % Tilt angle during cruise and resulting free stream velocity on x- and
    % z-axis in the body centered reference system
    [tilt_cr, ~] = RC_AoAandThrust(V_cr, MTOW);
    V_z_cr = V_cr * sin(tilt_cr) * 3.2808399;
    V_x_cr = V_cr * cos(tilt_cr) * 3.2808399;
    
    % Calculation of T_cr
    T_TO = 1.1 * MTOW * g / N_prop * 0.2248089431;  % lb
    T_cr = T_TO * 0.6; %cos(tilt_cr); % T_cr * 0.2248089431; %%%%%%%%%%%%% TBD  % lb
    T = T_cr;

    % Blade geometry
    lin_twist = -38;
    theta_tip = 10;
    
    % Induced velocity at rotor disk
    V_i_imp = sqrt(T/(2*rho_imp*pi*R_imp^2)); %induced velocity at the rotor

    % Variables and lists used for iteration
    RPM_list = 500:100:1500;
    rot_angles = 10:10:360;
    L_sum = 0;
    RPM_opt = RPM_list(end);

    % Matrix used for plotting
    dldr = zeros(numel(rot_angles), nr_stations);
    for RPM=RPM_list
        omega = RPM * 2 * pi / 60;
        i =  1;
        for rot_deg=rot_angles

            rot_rad = rot_deg * pi / 180;

            % Variables used for iteration
            L_blade = 0;
            r = R_hub_imp;

            % List used for plotting
            r_list = [];
            for station=1:nr_stations
                % Definition of blade section
                r = r + dr;

                % Local velocity of blade section
                V_blade = omega * r;
                V = sqrt((V_z_cr+V_i_imp)^2 + (V_blade+cos(rot_rad) * V_x_cr)^2);
                
                % Local pitch angle
                theta_local_deg = theta_tip - (1-(r-R_hub_imp)/(R_imp-R_hub_imp)) * lin_twist;  % deg
                theta_local = theta_local_deg * pi / 180;
                
                % Local angle of attack
                gamma = atan((V_z_cr+V_i_imp)/(V_blade+cos(rot_rad) * V_x_cr));
                alpha = theta_local - gamma;
                alpha_deg = alpha * 180 / pi;

                % Determination of local Cl value
                Cl = polyval(Cl_polar,alpha_deg);
                if alpha_deg < alpha_min || alpha_deg>alpha_stall
                    Cl = 0;
                end

                % Calculation of locally generated lift
                dL = 0.5 * Cl * rho_imp * V * V * C_imp * dr;
                dL_z = dL * cos(gamma);
                L_blade = L_blade + dL_z;
                
                % For plotting
                dldr(i, station) = dldr(i, station) + dL_z * dr;
                r_list(end+1) = r;
            end
            
            % Summation of lift produced by all element blades at each
            % rotation angle
            L_sum = L_sum + L_blade * B_prop;
            i = i + 1;
    
        end

        % Taking the average of produced lift over all rotation angles
        L = L_sum / numel(rot_angles);
        dldr = dldr / numel(rot_angles);

        % Finding the first RPM for which the lift is sufficient
        if L>T && RPM < RPM_opt
            RPM_opt = RPM;
            fprintf('RPM_opt for cruise = %f \n', RPM_opt)
            break
        end
    end
    
    % Plotting
    r_list = r_list / 3.2808399;
    dldr_list = dldr / 0.2248089431;

    fig1 = figure(1);
    surf(r_list,rot_angles,dldr_list)
    xlabel('r [m]');
    ylabel('Angle of rotation [deg]');
    zlabel('$\Delta L / \Delta R$ [N/m]','Interpreter','latex');
    %savefig(fig1,'Figures/ControlPropellerFig3')
end
