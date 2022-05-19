clear all
close all
clc

global l_pyl R_pyl N_prop D

inputs;


parasite_drag();
RC_AoAandThrust(V_cr, D_q_tot_x, rho, MTOW, g);

PowerReq(MTOW,N_prop,R_prop,V_cr)


