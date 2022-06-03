%% Create different cross-sections throughout the fuselage
classdef FL_Crosssection
    properties
        n
        X
        Vz
        My
        t = 0.002
    end
    methods
        function obj = FL_Crosssection(n, pos_x)
            obj.n = n;
            obj.X = pos_x;
            obj.Vz = 45 * pos_x;      % Wrong equation
            obj.My = 1-pos_x+pos_x^2; % Wrong equation
        end
    end
end