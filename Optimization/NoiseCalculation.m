function [SPL_mat] = NoiseCalculation(MTOW, RPM_opt_list)
    
    inputs;
    
    
    % Noise estimation

    sos = 343;  % m/s, speed of sound
    R_eff = (R_prop-(R_hub+0.0875));
    p_ref = 2 * 10^(-5);  % Pa
    K2 = 0.01206 * 3.2808399^3;
    sigma = (R_prop* C_prop * B_prop) / (pi * R_prop^2);  % solidity ratio

    harmonics = [1, 2, 4];
    
    ang_min = 90;
    ang_max = 180;
    dist_min = 20;
    dist_max = 200;
    d_ang = 10;
    d_dist = 20;

    dim_ang = (ang_max - ang_min) / d_ang + 1;
    dim_dist = (dist_max - dist_min) / d_dist + 1;

    SPL_mat = zeros(numel(harmonics), (dim_ang * dim_dist));
    p_sum = zeros(dim_ang, dim_dist);
    
    
    % Defining of distance and angle vectors

    dist_vec = dist_min:d_dist:dist_max;
    for i=1:dim_ang-1
        dist_vec = cat(1, dist_vec, dist_min:d_dist:dist_max);
    end
    disp(dist_vec)

    ang_vec_deg = ones(1, 10) * ang_min;
    for i=1:dim_ang-1
        ang_vec_deg = cat(1, ang_vec_deg, ones(1, 10) * (ang_min + i * d_ang));
    end
    disp(ang_vec_deg)
    ang_vec = ang_vec_deg * pi / 180;

    RPM_opt_list = 800;
    
    % Rotational noise
    for i=1:numel(RPM_opt_list)
        omega_opt = RPM_opt_list(i) * 2*pi/60;
        T = 1.1 * MTOW * g / N_prop;
        for m=harmonics
            J_mB = besselj(m*B_prop, m * B_prop * omega_opt ./ sos * R_eff .* sin(ang_vec));
            p_mL = (m * B_prop * omega_opt) ./ (2*sqrt(2)*pi * sos * dist_vec) .* (T * cos(ang_vec) - Q * sos / (omega_opt * R_eff^2)) .* J_mB;
            p_mT = (-rho * (m * B_prop * omega_opt)^2 * B_prop) ./ (3*sqrt(2)*pi*dist_vec) * ...
                C_prop * t_prop * R_eff .* J_mB;
            


            % dB to dBA correction factor (A-weighting)
            f = 2 * pi * m * omega_opt * B_prop;
            A_f = 12194^2 * f.^4 ./ ((f.^2 + 20.6^2) .* ...
                sqrt((f.^2 + 107.7^2).*(f.^2 + 737.9^2)) .* (f.^2 + 12194^2));

            p = (p_mL.^2 + p_mT.^2) ./ p_ref^2 + A_f^2;
                    

        end        
        p_sum = p_sum + p;
        p_sum(p_sum<0) = 0;


        % Vortex noise
        % dB to dBA correction factor (A-weighting)
        f = 2 * pi * 1 * omega_opt * B_prop;
        A_f = 12194^2 * f.^4 ./ ((f.^2 + 20.6^2) .* ...
            sqrt((f.^2 + 107.7^2).*(f.^2 + 737.9^2)) .* (f.^2 + 12194^2));

        SPL_vortex = 20 * log10(K2 * (omega_opt*R_prop)./(rho*dist_vec).*sqrt(N_prop * T / sigma * T / (pi * R_prop^2)) + A_f);
        fprintf('a-f = %f', A_f)
        disp(SPL_vortex)

    end

    SPL_rot = 10 * log10(N_prop * p_sum + SPL_vortex);

    SPL = 10 * log10(10.^(SPL_rot/10) + 10.^(SPL_vortex/10));

    SPL(end, :) = zeros(1, dim_dist);
    disp(SPL_rot)
    disp(SPL)


end

