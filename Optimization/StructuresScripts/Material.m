classdef Material
    %PART Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        density
        cost
        sigma_t
        sigma_y
        E_modulus
        tau
        G_modulus
    end
    
    methods
        function obj = Material(density, cost, tensile_strength, ...
                yield_strength, E_modulus, shear_strength, G_modulus)
            obj.density = density;
            obj.cost = cost;
            obj.sigma_t = tensile_strength;
            obj.sigma_y = yield_strength;
            obj.E_modulus = E_modulus;
            obj.tau = shear_strength;
            obj.G_modulus = G_modulus;
        end
        
    end
end

