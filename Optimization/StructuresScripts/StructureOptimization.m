function [outputArg1,outputArg2] = StructureOptimization(MTOW)
    
    n_ult = 3;

    % define lengths of the beams: [l1, l2, l3, l4, l5, l6, l7, l8]
    % define initial value of r (will be iterated n times)
    % define range of thickness to iterate for: [t1, t2, t3, ...]

    lengths = [1.2, 1.4, 1.6, 2.];
    t_list = [0.003, 0.004, 0.005, 0.006];
    r_init = 0.005;

    load = Load(MTOW * n_ult, V_wind_avg, F_z, torque);
    
    for length=lenghts
        beam = Beam(length, r_init, thickness);
        [Vx, Vy] = STRUC_Shear(pos_z, beam, load);
    
    end


    
end

