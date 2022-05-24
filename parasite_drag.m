function [CD0, D_q_tot_x] = parasite_drag()
inputs;
%global l_pyl R_pyl N_prop D R_prop 
%For a quadrotor. Found at https://ntrs.nasa.gov/api/citations/20180003381/downloads/20180003381.pdf
CD_fus = 0.05; %use the fuselage crossectional area. CD is assumed from an ellipse.
CD_rot = 0.0045; %use rotor disk area
CD_pyl = 0.025 ; %use pylon wet area
D_q_landinggear = 0.2*0.3048^2; %Landing gear CDA [m^2]

S_pylon = l_pyl * 2*pi *R_pyl*(N_prop); % Estimated pylon wet area [m^2]

%Own design estimated from above parameters
S_fus = pi*D^2/4 ;%Fuselage cross-sectional area [m^2]
S_disk = R_prop^2 * pi * N_prop   ;%Rotor disk area [m^2]
% Parasite CDA
D_q_tot_x = (CD_fus*S_fus + CD_rot*S_disk + (N_prop)*CD_pyl*S_pylon + D_q_landinggear);
% Assume that the reference area is the fuselage crosssectional area
CD0 = D_q_tot_x/S_fus; %parasitic drag coefficient
end