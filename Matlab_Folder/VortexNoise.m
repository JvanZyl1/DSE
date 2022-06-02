function SPL = VortexNoise(omega,R,rho,S,N,T,s,A)
%omega is rotational velocity of rotor [rad/s]
% R is propeller radius [m]
% rho is density [kg m^-3]
% S is the radial distance to the observer [m]
% N is amount of rotors [-]
% T is the thrust per one rotor [N]
% s is the solidity [-]
% A is the rotor disk area [m^2]

%Get them to imperial units
rho = rho/515.4;
R = R/0.3048;
S = S/0.3048;
T = T*1.36;
A = A/0.3048^2;
K2 = 1.206e-2;
SPL = 20*log10(K2*(omega*R)/(rho*S)*sqrt(N*T^2/(s*A)));
end