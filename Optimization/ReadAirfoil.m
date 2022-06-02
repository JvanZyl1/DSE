function [airfoil] = ReadAirfoil(fileName)
    % this function reads the airfoil geomtry and computes the
    % cross-sectional volume based off the dimensions i dat. file 
    fileName = 'n0012.dat';
    data = readmatrix(['Excel/' fileName]);
    dim = data(1,1);
    xys = data(2:end,:);
    top = xys(1:dim,:);
    bottom = xys((dim+1):end,:);

    thicks = top(:,2) - bottom(:,2);
    A = trapz(top(:,1),thicks);
    airf = [top(:,1) bottom(:,2) top(:,2)];

    airfoil = struct('Area',A,'Airfoil',airf);

    % plot the geometry
    %plot(top(:,1),top(:,2));
    %hold on
    %plot(bottom(:,1),bottom(:,2));