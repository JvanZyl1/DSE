function [] = ReynoldsNumber(RPM_list)
inputs;

nr_stations = 20;
dr = (R_prop - R_hub) / nr_stations;
omega_list = RPM_list * 2 * pi / 60;
r_list = R_hub:dr:R_prop;

for omega=omega_list
    for r=r_list
        V = r * omega; 
        if V>265
            %fprintf('Tip speed exceeds 0.8M at r = %f \n', r)
            break
        end
        Re = rho * V * C_prop / (1.81 * 10^(-5));
        %disp(r/0.12);
        %disp(Re);
        if r==R_prop
            %fprintf('Tip speed does not exceed 0.8M at %i RPM \n', omega_prop)
        end
    end
end

end

