function [max_powers, W_motors] = MotorSelection(MTOW)
    % This script calculates the powers required per motor for emergency
    % conditions, thus for the critical cases where 2 propellers fail.
    
    inputs;
    
    % Distances from centers of propellers to c.g. on x-axis
    x_b = x_cg - R_prop;  % Distance for back propellers
    x_tf = (R_prop * 3 - prop_clearance) - x_cg;  % Distance for top front propeller
    x_bf = (6 - R_prop) - x_cg;  % Distance for bottom front propeller
    
    % Emergency case 1: Failure front bottom propellers
    T_tf = x_b/2 * 1.1 * 1.5 * MTOW * g / (x_tf + 2 * x_b / 3);

    % Emergency case 2: Failure of top front propellers
    T_bf = x_b/2 * 1.1 * 1.5 * MTOW * g / (x_bf + 2 * x_b / 3);

    % Emergency case 3: Failure of two of the back propellers
    T_b = (x_tf + x_bf)/4 * 1.1 * 1.5 * MTOW * g / (x_b + (x_tf + x_bf) / 3);

    % Emergency case 4: Failure of 2 propellers on the same side of the x-axis
    T_side = 0.25 * 1.1 * 1.5 * MTOW * g;

    %disp([T_tf, T_bf, T_b])

    if T_tf<T_side
        T_tf = T_side;
    elseif T_bf<T_side
        T_bf = T_side;
    elseif T_b<T_side
        T_b = T_side;
    end

    %disp([T_tf, T_bf, T_b])

    P_tf = (((T_tf * V_TO)/2) * (sqrt(1+(2 * T_tf)/(rho * V_TO^2 * A_disk))))/eta_final ; 
    P_bf = (((T_bf * V_TO)/2) * (sqrt(1+(2 * T_bf)/(rho * V_TO^2 * A_disk))))/eta_final ; 
    P_b = (((T_b * V_TO)/2) * (sqrt(1+(2 * T_b)/(rho * V_TO^2 * A_disk))))/eta_final ; 

    %fprintf('Max power required for each engine: Front bottom = %f \n Front top = %f\n Back motors = %f \n', P_bf, P_tf, P_b)
    max_powers = [P_tf, P_bf, P_b];
    %fprintf('max powers = %f %f %f', max_powers)
    emrax_weight = [0, 7.2, 9.3, 12.3, 20.3, 40];
    emrax_power = [0, (32+60)/2, (40+75)/2, (55+100)/2, (85+160)/2, (100+190)/2] * 1000;
    W_motors = zeros(1, N_prop);
    for i=1:numel(max_powers)
        max_power = max_powers(i);
        %disp(max_power)
        for j=2:numel(emrax_weight)
            if max_power<emrax_power(j)
                %W_m = (max_power - emrax_power(j-1)) / (emrax_power(j) - emrax_power(j-1));
                W_m = interp1(emrax_power, emrax_weight, max_power);
            end
        end
        if i == 1
            W_motors(1) = W_m;
            W_motors(2) = W_m;
        elseif i == 2
            W_motors(3) = W_m;
            W_motors(4) = W_m;
        elseif i == 3
            W_motors(5) = W_m;
            W_motors(6) = W_m;
            W_motors(7) = W_m;
            W_motors(8) = W_m;
        end            
    end
    %fprintf('W_motors = %f %f %f %f %f %f %f %f\n', W_motors(1), W_motors(2), W_motors(3), W_motors(4), W_motors(5), W_motors(6), W_motors(7), W_motors(8))
end

