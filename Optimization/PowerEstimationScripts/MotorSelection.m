function [] = MotorSelection(MTOW)
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

end

