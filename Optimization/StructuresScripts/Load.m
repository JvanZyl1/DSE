classdef Load
    properties
        L
        D
        P
        T
    end
    
    methods
        function obj = Load(L, V_wind_avg, F_z, torque, rho, C_D)
            obj.L = L;
            obj.D = 0.5*C_D*rho*V_wind_avg^2;
            obj.P = F_z;
            obj.T = torque;
        end
        
    end
end

