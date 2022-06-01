function [Vx, Vy] = STRUC_Shear(pos_z, We, part, load)
    Vx = -load.D;
    Vy = part.W + We - load.L - part.W * pos_z / part.l;
end

