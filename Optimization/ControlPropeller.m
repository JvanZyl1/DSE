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

alpha = deg2rad(-12:2:12) ;  %NACA 0012 data below 
Cl = [-0.7967 -0.9268 -0.8043 -0.6567 -0.5073 -0.3402 0 0.3402 0.5073 0.6566 0.8043 0.9268 0.7967];
Cd = [0.08718 0.04819 0.03353 0.02488 0.02048 0.01942 0.02068 0.01942 0.02048 0.02488 0.03353 0.04819 0.08718]
Cl_polar = polyfit(alpha,Cl,3);
Cd_polar = polyfit(alpha,Cd,3);



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

