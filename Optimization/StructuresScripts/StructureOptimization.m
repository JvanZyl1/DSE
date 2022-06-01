function [W_beams] = StructureOptimization(MTOW, We)
    
    inputs;
    STRUC_input;

    load = Load(MTOW * g * n_ult * SF / N_prop, 0, 0, 1000, rho, C_D_beam);
    material = aluminium;

    r = r_init;
    W_beams = 0;
    i = 1;
    j = 1;
    pos_z = 0.5;
    n_iter = 10;
    for length=lengths
        %for pos_z=z_interval:1:z_interval
            %pos_z = pos_z * length;
        for thickness=thicknesses
            for n=1:n_iter
                beam = Beam(length, r, thickness, material);
                %disp([beam.l, beam.r, beam.t, beam.W])
                [Vx, Vy] = STRUC_Shear(pos_z, We, beam, load);
                [Mx, My] = STRUC_Moments(pos_z, We, beam, load);
                [r] = Radius(Vx, Vy, Mx, My, beam, load, material);

            end
            %fprintf('r = %f for t = %f \n', r, thickness)
            % Calculation of beam weight
            beam = Beam(length, r, thickness, material);
            W_beam = beam.W;
            
            % Checking if the beam weight for this thickness is better than
            % previous calculations
            if j==1
                W_beam_opt = W_beam;
                t_opt = thickness;
            end
            if W_beam < W_beam_opt
                W_beam_opt = W_beam;
                t_opt = thickness;
            end
            j = j + 1;
            %end
        end

        %fprintf('For beam %d and %d with length %f, the optimum thickness is %f,\n resulting in a beam weight of %f', i, i+1, length, t_opt, W_beam_opt)
        i = i + 2;
        
        % W_beam_opt is multiplied by 2 due to symmetry along the x-axis of
        % the vehicle
        W_beams = W_beams + 2 * W_beam_opt;
    end


    
end

