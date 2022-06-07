function [SPL_mat] = NoiseCalculation(MTOW, RPM_opt_list)
    
    inputs;
    
    
    % Noise estimation

    sos = 343;  % m/s, speed of sound
    R_eff = (R_prop-R_hub);
    p_ref = 2 * 10^(-5);  % Pa

    harmonics = 1:3;
    
    ang_min = 90;
    ang_max = 180;
    dist_min = 10;
    dist_max = 100;
    d_ang = 10;
    d_dist = 10;

    dim_ang = (ang_max - ang_min) / d_ang + 1;
    dim_dist = (dist_max - dist_min) / d_dist + 1;
    SPL_mat = zeros(numel(harmonics), (dim_ang * dim_dist));
    p_mL_arr = [];
    p_mT_arr = [];
    p_sum = zeros(dim_ang, dim_dist);
    
    dist_vec = dist_min:d_dist:dist_max;
    for i=1:dim_ang-1
        dist_vec = cat(1, dist_vec, dist_min:d_dist:dist_max);
    end
    disp(dist_vec)

    ang_vec = ones(1, 10) * ang_min;
    for i=1:dim_dist-1
        ang_vec = cat(1, ang_vec, ones(1, 10) * (ang_min + i * d_ang));
    end
    disp(ang_vec)

    RPM_opt_list = 800;
    
    % Rotational noise
    for i=1:numel(RPM_opt_list)
        omega_opt = RPM_opt_list(i) * 2*pi/60;
        T = 1.1 * MTOW * g;
        for m=harmonics
            J_mB = besselj(m*B_prop, m * B_prop * omega_opt ./ (sos * R_eff .* sin(ang_vec)));
            p_mL = (m * B_prop * omega_opt) ./ (2*sqrt(2)*pi * sos * dist_vec) .* ...
                (T * cos(ang_vec) - Q * sos / (omega_opt * R_eff^2)) .* J_mB;
            
            p_mT = (-rho * (m * B_prop * omega_opt)^2 * B_prop) ./ (3*sqrt(2)*pi*dist_vec) * ...
                C_prop * t_prop * R_eff .* J_mB;
        
            SPL = 10 * log10(N_prop * ((p_mL.^2 + p_mT.^2) ./ p_ref^2));

            p = (p_mL.^2 + p_mT.^2) ./ p_ref^2;

            %disp(J_mB)

        end        
        p_sum = p_sum + p;

    end

    SPL = 10 * log10(N_prop * p_sum);
    disp(SPL)


end

