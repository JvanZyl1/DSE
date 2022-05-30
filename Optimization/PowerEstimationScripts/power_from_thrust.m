function [P] = power_from_thrust(T, A_cont)
inputs;
% Global V_wind_avg, rho, eta_final

Np;
P = (((T * V_wind_avg) / 2) * (sqrt(1 + (2 * T) / (rho * V_wind_avg^2 * A_cont)))) / eta_final;
    
end