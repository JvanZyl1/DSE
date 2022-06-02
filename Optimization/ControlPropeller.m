%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Control Propeller Design Module %%%
%%%  Alex Krochak 2022 DSE Group 5  %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% This function calculates a control rotor geometry for the Veatle based
% off external inputs:
% INPUTS: 
% [R - tip radius; R1 - hub radius; V_gust - velocity through the rotor
%  theta - input pitch angle of the blade; b - number of blades;
%  T_con - MAX torque of the contorl motors in Nm; 
%  rho_blade - blade material density]
% OUTPUTS:
% [Blade geometry, Thrust, Lift distribution, etc.]
clear 
inputs;


R = 0.2;
R1 = 0.10; %hub radius
V_gust = 25; %this is the velocity  through a control propeller due to the gust hitting a vehicle.
c = 2 / 100; % chord length in metres
T = 20;    %control thrust
b = 5;      %number of blades
theta = 20  ; % pitch in degrees, spanwise invariant.
M_tip = 0.8;    % maximum tip Mach number
n_iter = 30;
T_con = 90;     % torque of control motors in Nm (max, not cont). 
rho_blade = 2000; %blade material density in kg/m3 . carbon fibre 

%define the airfoil polars:
fileName = 'xf-n0012-il-50000-n5.csv';
fileAirfoil = 'n0012.dat'
[alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
%plot(alpha,polyval(Cl_polar,alpha))

V_a = 343; %speed of sound at sea level

A = pi * R^2;
V_tip = 0.8 * V_a;
omega = V_tip / R; %angular velocity, rad/s
th = deg2rad(theta);
rs = R1:0.01:R;

for i=1:n_iter
    V_i = sqrt(T/(2*rho*A)) + V_gust; %induced velocity at the rotor
    phis = atan(V_i ./ (omega .* rs));
    
    alphas_eff = (th - phis);
    %check the effective alphas:

    Cls_theta = polyval(Cl_polar,rad2deg(alphas_eff));
    Cds_theta = polyval(Cd_polar,rad2deg(alphas_eff));
    dldr = 0.5 * rho * omega^2 * R^2 * Cls_theta * c;  %Prouty page 14
    L = trapz(rs,dldr);
    T_upd = L*b
    T = (T_upd + T) * 0.5; 
    Ts(i) = T;
    V_is(i) = V_i;
end

if rad2deg(alphas_eff(end)) > 12 || rad2deg(alphas_eff(1)) < -12; 
    msg = 'The blade has stalled !!!'
    plot(rad2deg(alphas_eff));
    error(msg)
end

T_ult = Ts(end);
disp(T_ult)
plot(rs,dldr);

%% Calculate the inertia and force respopnse. 
% Here we assume that blade is made up of a solid cylinder rod connecting
% it with the blade element, which has the shape of NACA0012 airfoil and
% thickness equal to the cylinder rod diameter. Material density is
% assumed, all things are completely solid.

% External dimensions 

V_cyl = R1 * pi * (c * 0.5 * 0.12)^2;
M_cyl = rho_blade * V_cyl;

A_airf = ReadAirfoil('fileAirfoil').Area * c^2;
Airfoil = ReadAirfoil('fileAirfoil').Airfoil;
V_airf = A_airf * (R-R1);
M_airf = V_airf * rho_blade;

% claculate inertia
I_airf = ((R1^2) * M_airf) + (0.3333 * ((R-R1)^2) * M_airf); % I balde = I_parall axis + I_blade
I_cyl = (0.3333 * (R1^2) * M_airf); 
I_blade = I_airf + I_cyl;
I_total = b * I_blade;
M_total = b * (M_airf + M_cyl);
disp(I_total)
disp(M_total)
ang_acc = T_con / I_total;
tau = omega / ang_acc;
disp(tau);


%% make a nice plot of airfoil
dim = length(Airfoil(:,3));
X = c*[Airfoil(:,1) Airfoil(:,1)];
Y = repmat([R1 R],dim,1);
Zt = c*[Airfoil(:,2) Airfoil(:,2)];
Zb = c*[Airfoil(:,3) Airfoil(:,3)];
% cylinder

fig = figure(1)
surf(X,Y,Zt)
hold on 
surf(X,Y,Zb)
colormap(gray);
daspect([1 1 1]);

[Zc,Xc,Yc] = cylinder(c*0.12/2);
Yc = Yc * R1;
Xc = Xc + c*0.3;
surf(Xc,Yc,Zc)
ylabel('R [m]');
zlabel('t [m]');
hold off
view(2)