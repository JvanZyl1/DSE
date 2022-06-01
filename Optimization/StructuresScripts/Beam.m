classdef Beam
    properties
        name = "beam"
        K = 8;
        l
        r
        t
        W
        Ixx
        Iyy
    end

    methods
        function obj = Beam(length, radius, thickness, material)
            obj.l = length;
            obj.r = radius;
            obj.t = thickness;
            obj.W = pi * obj.l * ((obj.r + obj.t/2)^2 - (obj.r - obj.t/2)^2) * material.density;
            obj.Ixx = thickness * radius ^ 3;
            obj.Iyy = thickness * radius ^ 3;
        end

        %function W_beam = weightest(obj, material)
        %    W_beam = pi * obj.l * ((obj.r + obj.t/2)^2 - (obj.r - obj.t/2)^2) * material.density;
        %end
    end
end

