function [SPL_mat] = NoiseCalculation(MTOW)
    
    inputs;

    %N_prop = 0;
    %R_prop = 0.4;
    %C_prop = 0;
    
    if MTOW <= 0
        error('MTOW is not valid')
    end

    % Noise estimation

     R_prop = 13.2 / 3.2808399;
     RPM_list = 680 / R_prop;
     R_hub = 0.2 * R_prop - 0.0875;
     C_prop = 0.56 / 3.2808399;
     t_prop = 0.12 * C_prop;
     B_prop = 5;
     N_prop = 1;
     MTOW = 3000 * 0.45359237 * g;
     h_cr = 500 / 3.2808399; %ft
     Q = 800;

%     R_prop = 420 * 0.0254 / 2;
%     RPM_list = 413;
%     R_hub = 0.2 * R_prop - 0.0875;
%     C_prop = 10.75 * 0.0254;
%     t_prop = 0.12 * C_prop;
%     B_prop = 4;
%     N_prop = 1;
%     MTOW = 6000 * 0.45359237;
%     h_cr = 500 / 3.2808399;
%     Q = 1000;

    sos = 343;  % m/s, speed of sound
    R_eff = (R_prop-(R_hub+0.0875));
    p_ref = 2 * 10^(-5);  % Pa
    K2 = 0.01206 * 3.2808399^3;
    fprintf('K2 = %f \n', K2)
    sigma = (R_prop * C_prop * B_prop) / (pi * R_prop^2);  % solidity ratio

    harmonics = 1:1:20;
    
    ang_min = 180;
    ang_max = 105;
    d_ang = -1;

    dim_ang = (ang_max - ang_min) / d_ang + 1;
    dim_dist = dim_ang;
    
    SPL_mat = zeros(numel(harmonics), (dim_ang * dim_dist));

    ang_vec_deg = ones(1, 10) * ang_min;
    for i=1:dim_ang-1
        ang_vec_deg = cat(1, ang_vec_deg, ones(1, 10) * (ang_min + i * d_ang));
    end
    ang_vec = ang_vec_deg * pi / 180;
    dist_vec = h_cr ./ sin(ang_vec - pi/2);
    %disp(dist_vec)
    %disp(ang_vec_deg)

%     dist_vec = dist_min:d_dist:dist_max;
%     for i=1:dim_ang-1
%         dist_vec = cat(1, dist_vec, dist_min:d_dist:dist_max);
%     end

    %disp(ang_vec_deg)
    
    
    
%     % Defining of distance and angle vectors
%     dist_vec = [200, 400, 630, 1000, 2000, 4000, 6300, 10000, 16000, 25000];
%     dist_vec = sqrt(ones(size(dist_vec)) .* h_cr^2  + dist_vec.^2) ./ 3.2808399;
%     dist_vec_row = dist_vec;
%     for i=1:9
%         dist_vec = cat(1, dist_vec, dist_vec_row);
%     end
%     disp(dist_vec)
% 
%     ang_vec = atan2(ones(10, 10) * h_cr, dist_vec) + ones(10, 10) * pi/2;
%     ang_vec_deg = ang_vec * 180 / pi;
%     disp(ang_vec_deg)

    %ang_vec = 160 / 180 * pi;
    %dist_vec = h_cr;


    %dist = 50;
    %dist_vec = ones(size(ang_vec)) * dist;
    %dist_vec = cat(1, dist_vec, flip(dist_vec(2:end, :), 1));
    %dist_vec = cat(2, dist_vec, flip(dist_vec(:, 2:end), 2));

    %ang_vec = cat(1, ang_vec, flip(ang_vec(2:end, :), 1));
    %ang_vec = cat(2, ang_vec, flip(ang_vec(:, 2:end), 2));

    %dist_vec = dist_vec ./ cos(pi - ang_vec);
    %disp(dist_vec)
    %disp(ang_vec_deg)
    
    %RPM_list = 800;
    T = 0.6 * 1.1 * MTOW * g / N_prop;
    
    % Rotational noise
    for i=1:numel(RPM_list)
        omega_opt = RPM_list(i) * 2*pi/60;
        SPL_rot_old = 0;
        for m=harmonics
            J_mB = besselj(m*B_prop, m * B_prop * omega_opt ./ sos * R_eff .* sin(ang_vec));
            p_mL = (m * B_prop * omega_opt) ./ (2*sqrt(2)*pi * sos * dist_vec) .* ...
                (T * cos(ang_vec) - Q * sos / (omega_opt * R_eff^2)) .* J_mB;
            p_mT = (-rho * (m * B_prop * omega_opt)^2 * B_prop) ./ (3*sqrt(2)*pi*dist_vec) * ...
                C_prop * t_prop * R_eff .* J_mB;
            %disp(p_mL)
            %disp(p_mT)

            % dB to dBA correction factor (A-weighting)
            [A_f] = A_Weighting(omega_opt, B_prop, m);
            %fprintf('A_f = %f \n', A_f)

            p = (p_mL.^2 + p_mT.^2) ./ p_ref^2;
            SPL_rot_new = 10 * log10(N_prop * p) + A_f;
            SPL_rot = 10 * log10(10.^(SPL_rot_old/10) + 10.^(SPL_rot_new/10));
            SPL_rot_old = SPL_rot;
            %fprintf('it = %f \n', 1)
            %disp(SPL_rot)
        end        
    end

    %SPL_rot = 10 * log10(N_prop * p_sum);
    [A_f] = A_Weighting(omega_opt, B_prop, 1);
    %disp(A_f)
    SPL_vortex = 20 * log10(K2 * (omega_opt*R_prop)./(rho*dist_vec).*sqrt(N_prop * T / sigma * T / (pi * R_prop^2))) + A_f;
    %disp(SPL_vortex)
    SPL = 10 * log10(10.^(SPL_rot/10) + 10.^(SPL_vortex/10));

    %SPL(end, :) = zeros(1, dim_dist);
    %disp(SPL)
    SEL = 0;
    noise_list = transpose(SPL(:, 1));
    for noise=noise_list
        SEL = 10 * log10(10^(SEL/10) + 10^(noise/10)); 
    end
    SEL_total = 10 * log10(10^(SEL/10) + 10^(SEL/10)); 
    %fprintf('SEL = %f \n', SEL)

end

