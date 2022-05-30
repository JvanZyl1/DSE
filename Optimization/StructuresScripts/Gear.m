classdef Gear

    properties
        name = 'gear'
        area
        length
        radius
    end
    
    methods
        function obj = Beam(length, radius, thickness)
            obj.l = length;
            obj.r = radius;
            obj.t = thickness;
            obj.We = 0;
            obj.self.area = 2 * pi * thickness * radius;
        end
    end
end

