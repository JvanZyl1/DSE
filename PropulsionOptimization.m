clear all
close all
clc

% global l_pyl R_pyl 

inputs;
MTOW = 700;  % kg

n_iter = 10;
for i=1:n_iter
    % Thrust power estimation
    [P_cruise, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr);
    
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    P_cont_max = (((dist_force * V_wind_avg) / 2) * (sqrt(1 + (2 * dist_force) / (rho * V_wind_avg^2 * A_disk_cont)))) / eta_final;
    
    % Weight estimation
    [BatWt, E_total] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
    [PropWt] = propulsiongroup_mass(P_TOL);
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, ~, ~] = controlgroup_mass(P_cont_max);
    W_beams = 60;  % TODO
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
end

fprintf('Old method: MTOW = %f \n',MTOW)

for i=1:n_iter
    % Thrust power estimation
    [~, P_TOL, P_cont_avg] = PowerReq(MTOW, V_cr);
    P_cruise = PowerViaDrag(V_cr, MTOW) * 1000;
    % Control power estimation: separate power required on a continuous basis during TOL and maximum power required during strongest gust loads
    P_cont_max = (((dist_force * V_wind_avg) / 2) * (sqrt(1 + (2 * dist_force) / (rho * V_wind_avg^2 * A_disk_cont)))) / eta_final;
    
    % Weight estimation
    [BatWt, E_total] = BatteryMassFun(V_cr, P_cruise, P_TOL, P_cont_avg);
    [PropWt] = propulsiongroup_mass(P_TOL);
    [FuseWt] = fuselagegroup_mass(MTOW, V_cr);
    [ContWt, ~, ~] = controlgroup_mass(P_cont_max);
    W_beams = 60;  % TODO
    MTOW = W_PL + BatWt + PropWt + FuseWt + ContWt + W_beams;
end

fprintf('New method: MTOW = %f \n',MTOW)


omega_list = 500:100:3500;
r_list = 0:0.12:R_prop;

for omega_prop=omega_list
    omega_prop=1000;
    for r=r_list
        V = r * omega_prop * 2 * pi / 60; 
        if V>265
            %fprintf('Tip speed exceeds 0.8M at r = %f \n', r)
            break
        end
        Re = rho * V * C_prop / (1.81 * 10^(-5));
        disp(Re)
        if r==R_prop
            %fprintf('Tip speed does not exceed 0.8M at %i RPM \n', omega_prop)
        end
    end
end





fprintf('Battery weight: %f \n',BatWt)
fprintf('MTOW: %f \n',MTOW)
fprintf('Required energy: %f \n',E_total)
fprintf('P_cruise = %f, and P_TOL = %f \n',P_cruise,P_TOL)