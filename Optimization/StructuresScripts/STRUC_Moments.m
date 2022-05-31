function [Mx, My] = STRUC_Moments(pos_z, We, part, load)

    M_ax = (part.W / 2 + We - load.L) * part.l;
    Mx = (part.W + We - load.L) * pos_z - part.W * pos_z ^ 2 / (2 * part.l) - M_ax;

    M_ay = part.l * load.D * part.r * 2 * load.L;
    My = M_ay - M_ay * pos_z / part.l + load.T;

end

