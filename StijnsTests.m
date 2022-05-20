clear all
close all
clc

%global l_pyl R_pyl N_prop D

inputs;


parasite_drag();
RC_AoAandThrust(V_cr, rho, MTOW, g);

[P_cr,P_takeoff] = PowerReq(MTOW,N_prop,R_prop,V_cr)


