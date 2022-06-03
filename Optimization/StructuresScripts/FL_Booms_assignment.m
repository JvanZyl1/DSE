clc

%% Booms assignment

boom(1) = FL_Booms(1, 0.2, sin(2*pi/10*1), cos(2*pi/10*1), 0.010);
boom(2) = FL_Booms(1, 0.2, sin(2*pi/10*2), cos(2*pi/10*2), 0.010);
boom(3) = FL_Booms(1, 0.2, sin(2*pi/10*3), cos(2*pi/10*3), 0.010);
boom(4) = FL_Booms(1, 0.2, sin(2*pi/10*4), cos(2*pi/10*4), 0.010);
boom(5) = FL_Booms(1, 0.2, sin(2*pi/10*5), cos(2*pi/10*5), 0.010);
boom(6) = FL_Booms(1, 0.2, sin(2*pi/10*6), cos(2*pi/10*6), 0.010);
boom(7) = FL_Booms(1, 0.2, sin(2*pi/10*7), cos(2*pi/10*7), 0.010);
boom(8) = FL_Booms(1, 0.2, sin(2*pi/10*8), cos(2*pi/10*8), 0.010);
boom(9) = FL_Booms(1, 0.2, sin(2*pi/10*9), cos(2*pi/10*9), 0.010);
boom(10)= FL_Booms(1, 0.2, sin(2*pi/10*10), cos(2*pi/10*10), 0.010);

sz = size(boom, 2);


for i = 1:sz
    if i == sz
        b1 = sqrt((boom(1).Y - boom(i).Y)^2 + (boom(1).Z - boom(i).Z)^2);
        b2 = sqrt((boom(i).Y - boom(i-1).Y)^2 + (boom(i).Z - boom(i-1).Z)^2);
        areaB = boom(i).A + boom(i).t * b1/6 * (2+1) + boom(i).t * b2/6 * (2+1);
    elseif i == 1
        b1 = sqrt((boom(i+1).Y - boom(i).Y)^2 + (boom(i+1).Z - boom(i).Z)^2);
        b2 = sqrt((boom(i).Y - boom(sz).Y)^2 + (boom(i).Z - boom(sz).Z)^2);
        areaB = boom(i).A + boom(i).t * b1/6 * (2+1) + boom(i).t * b2/6 * (2+1);
    else
        b1 = sqrt((boom(i+1).Y - boom(i).Y)^2 + (boom(i+1).Z - boom(i).Z)^2);
        b2 = sqrt((boom(i).Y - boom(i-1).Y)^2 + (boom(i).Z - boom(i-1).Z)^2);
        areaB = boom(i).A + boom(i).t * b1/6 * (2+1) + boom(i).t * b2/6 * (2+1);
    end
    boom(i).area(10); 
end

figure
ax1 = nexttile;
plot(ax1,[boom.Y], [boom.Z])
title(ax1,'Cross-section with booms')
xlabel(ax1, 'y')
ylabel(ax1, 'z')



