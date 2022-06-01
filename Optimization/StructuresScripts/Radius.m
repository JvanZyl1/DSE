function [r] = Radius(Vx, Vy, Mx, My, part, load, material)

    % Bending in lift-direction for TENSION
    r1 = (load.P + sqrt(abs(((load.P) ^ 2) + 4 * 2 * pi * part.t * material.sigma_y * 2 * pi * Mx))) / (4 * pi * part.t * material.sigma_y);

    % Bending in lift-direction for COMPRESSION
    if part.name == "beam"
        r2 = (abs(Mx * part.l ^ 2) / (part.t * pi ^ 2 * material.E_modulus)) ^ (1 / 4);
    else
        r2 = (load.P * part.l ^ 2 / (2 * pi ^ 3 * part.t)) ^ 3;
    end

    % Bending in axial-direction for TENSION
    r3 = (abs(My) + sqrt((My) ^ 2 + 4 * 2 * pi * part.t * material.sigma_y * 2 * pi * load.P)) / (4 * pi * part.t * material.sigma_y);

    % Bending in axial-direction for COMPRESSION
    r4 = (abs(My * part.l ^ 2) / (part.t * pi ^ 2 * material.E_modulus)) ^ (1 / 4);

    % Shear in lift-direction
    r5 = (abs(Vx / (-pi * part.t * material.tau))) ^ (1 / 3);
    
    % Shear in axial-direction
    r6 = (abs(Vy / (-pi * part.t * material.tau))) ^ (1 / 3);

    r = max([r1, r2, r3, r4, r5, r6]);
end

