"C.G. Estimation"
from inputs import *
import MassEstimation as ME

'''
CG estimations, can be based on either with wing or without wing. (Set wing mass to 0, might hardcode this later)
Needs some iteration for total mass etc 
Battery Needs to be included 
Cables assumed to be in line with engine for now, should almost change nothing in CG
'''

#Inputs
M_Fuselage=ME.FuselageMassFun(l_t, V_cr, D, l)+ME.FurnishingMassFun(W_PL)
M_Landinggear=ME.LandingGearMassFun(W_MTOW)
M_Prop,_=ME.PropGroupMassFun(N_prop, R_prop, B_prop, P_cruise)
Props=N_prop
M_Wing,_=ME.WingGroupMassFun(W_MTOW, W_PL, b, Lambda, S, t_chord, n_ult)
M_Tail,_=ME.TailplaneGroupFun(S_h,S_v,n_ult)
M_Payload=250 #[kg}


#For now based on estimations from Ehang
#h_Landinggear= 0.4 #[m]
#h_Fuselage= 1.2 #[m]
#h_Prop= 0.5 #[m]
#h_Wing= 0 #[m]
#h_Tail= 0 #[m]
#h_Payload= 1.7 #[m]

#Based on Kittyhawk
h_Landinggear= 0.6 #[m]
h_Fuselage= 1.5 #[m]
h_Prop= 0.3 #[m]
h_Wing=1*0.12 #[m]
h_Tail= 1+0.75*0.12 #[m]
h_Payload= 1.7 #[m]


#Basic cg calculations
def CGcalculations(M_Fuselage, M_Landinggear, M_Prop, M_Wing, M_Tail, M_Payload, h_Landinggear, h_Fuselage, h_Prop, h_Wing, h_Tail, h_Payload):
  M_Total=M_Fuselage+M_Landinggear+M_Prop+M_Wing+M_Tail+M_Payload
  print('The total mass in [kg] is:', M_Total)
  #Estimations made by looking at Ehang and Kittyhawk
  cg_Landinggear= h_Landinggear/3
  cg_Fuselage= h_Landinggear+h_Fuselage/2
  cg_Prop= h_Landinggear
  cg_Wing= h_Landinggear+h_Fuselage/3
  cg_Tail= h_Landinggear+h_Tail*(2/3)
  cg_Payload= h_Landinggear+h_Payload/4

  cg_Total=(M_Fuselage*cg_Fuselage+M_Landinggear*cg_Landinggear+M_Prop*cg_Prop+M_Wing*cg_Wing+M_Tail*cg_Tail+M_Payload*cg_Payload)/M_Total
  print('The CG is located at a height of [m]:', cg_Total)
  return M_Total, cg_Total, cg_Landinggear, cg_Fuselage, cg_Prop, cg_Wing, cg_Tail, cg_Payload

