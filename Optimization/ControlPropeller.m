clear 
inputs;

% Cls = interp1(alpha,Cl,alphas);
% Cds = interp1(alpha,Cd,alphas);

R = R_cont;
R1 = 0.1; %hub radius
A = pi * R^2;

n_iter = 50;

c = 0.014 % chord length in metres
T = 500;    %control thrust

b = 2;      %number of blades
theta = 15; % pitch in degrees, spanwise invariant.
M_tip = 0.8;    % maximum tip Mach number
V_a = 343 %speed of sound at sea level

%define the airfoil polars:
fileName = 'xf-n0012-il-50000-n5.csv';
[alpha, Cl_polar, Cd_polar] = ReadPolar(fileName);
plot(alpha,polyval(Cl_polar,alpha))


V_tip = 0.8 * V_a;
omega = V_tip / R; %angular velocity, rad/s
th = deg2rad(theta);
rs = R1:0.01:R;

for i=1:n_iter
    v_i = sqrt(T/(2*rho*A)); %induced velocity at the rotor
    phi_t = atan(v_i / (omega * R));
    
    alphas_eff = (th - phi_t./(rs/R));
    
    Cls_theta = polyval(Cl_polar,alphas_eff);
    Cds_theta = polyval(Cd_polar,alphas_eff);
    dldr = 0.5 * rho * omega^2 * R *Cls_theta * c;
%     disp(rad2deg(phi_t));
    L = trapz(rs,dldr);
    T = L*b;
    Ts(i) = T;
    V_is(i) = v_i;
end
T_ult = Ts(end);
disp(T_ult)
plot(rs,rad2deg(alphas_eff));

