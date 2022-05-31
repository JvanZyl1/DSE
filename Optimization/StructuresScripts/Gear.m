classdef Gear

    properties
        name = 'gear'
        l
        r
        t
        We
        area
    end
    
    methods
        function obj = Gear(length, radius, thickness)
            obj.l = length;
            obj.r = radius;
            obj.t = thickness;
            obj.We = 0;
            obj.area = 2 * pi * thickness * radius;
        end
    end
end

