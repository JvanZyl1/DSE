clear 
inputs;

% Cls = interp1(alpha,Cl,alphas);
% Cds = interp1(alpha,Cd,alphas);

R = 0.3;
R1 = 0.15; %hub radius
A = pi * R^2;
i
V_gust = 25; %this is the velocity  through a control propeller due to the gust hitting a vehicle.

n_iter = 10;

c = 0.01; % chord length in metres
T = 400;    %control thrust

b = 2;      %number of blades
theta = 20  ; % pitch in degrees, spanwise invariant.
M_tip = 0.8;    % maximum tip Mach number
V_a = 343; %speed of sound at sea level

%define the airfoil polars:
fileName = 'xf-n0012-il-50000-n5.csv';
[alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
%plot(alpha,polyval(Cl_polar,alpha))


V_tip = 0.8 * V_a;
omega = V_tip / R; %angular velocity, rad/s
th = deg2rad(theta);
rs = R1:0.01:R;

for i=1:n_iter
    V_i = sqrt(T/(2*rho*A)) + V_gust; %induced velocity at the rotor
    phis = atan(V_i ./ (omega .* rs));
    
    alphas_eff = (th - phis);
    %check the effective alphas:
    if rad2deg(alphas_eff(end)) > 12 || rad2deg(alphas_eff(1)) < -12; 
        msg = 'The blade has stalled !!!'
        plot(rad2deg(alphas_eff));
        error(msg)
    end
    Cls_theta = polyval(Cl_polar,rad2deg(alphas_eff));
    Cds_theta = polyval(Cd_polar,rad2deg(alphas_eff));
    dldr = 0.5 * rho * omega^2 * R *Cls_theta * c;
    L = trapz(rs,dldr);
    T = L*b;
    Ts(i) = T;
    V_is(i) = V_i;
end
T_ult = Ts(end);
disp(T_ult)
plot(rs,dldr);

