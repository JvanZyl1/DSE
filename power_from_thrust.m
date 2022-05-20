function [P] = power_from_thrust(T, R_prop, N_prop)
inputs;
% Global V_wind_avg, rho, eta_final

A_disk = pi * R_prop^2 * N_prop;
P = (((T * V_wind_avg) / 2) * (sqrt(1 + (2 * T) / (rho * V_wind_avg^2 * A_disk)))) / eta_final;
    
end