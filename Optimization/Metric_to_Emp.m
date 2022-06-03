function [lengths_emp, velocities_emp, forces_emp, rho_emp] = Metric_to_Emp(lengths, velocities, forces)

    lengths_emp = 3.2808399 * lengths;
    velocities_emp = 3.2808399 * velocities;
    forces_emp = 0.2248089431 * forces;
    rho_emp = 0.002377;  % slug/ft^3\

end

