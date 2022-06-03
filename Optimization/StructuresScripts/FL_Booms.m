

classdef FL_Booms < FL_Crosssection
    properties
        Y
        Z
        sigma_y = 450e6
        Iyy
        Izz
        N = 0
        ind
        A
    end
    methods
        function obj = FL_Booms(n, pos_x, pos_y, pos_z, A)
            obj = obj@FL_Crosssection(n, pos_x)
            obj.A = A;
            obj.Y = pos_y;
            obj.Z = pos_z;
            %obj.B = obj.My / (obj.sigma_y * pos_y);
            %obj.Iyy = obj.B * pos_z^2;
            %obj.Izz = obj.B * pos_y^2;
            obj.N = obj.N + 1;
        end
        function amount(obj)
            disp("Hello " + obj.ElementIndex)
        end
        function B = area(boomarea)
            B = boomarea;
    end
end

