function [alpha, Cl_polar, Cd_polar] = ReadPolar(fileName)
    data = readmatrix(['../Excel/' fileName]);
    alpha = data(:,1);
    Cl = data(:,2);
    Cd = data(:,3);
    Cl_polar = polyfit(alpha,Cl,5);
    Cd_polar = polyfit(alpha,Cd,5);
    %plot(alpha,polyval(Cl_polar,alpha))
%xf-naca23012-il-1000000.csv