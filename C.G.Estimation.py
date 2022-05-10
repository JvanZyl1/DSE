"C.G. Estimation"

#Inputs

M_Fuselage=
M_Landinggear=
M_Prop=
Props=
M_Wing=
M_Tail=
M_Payload=250 #[kg}

#For now based on estimations from Ehang
h_Landinggear= 0.4 #[m]
h_Fuselage= 1.2 #[m]
h_Prop= 0.5 #[m]
h_Wing= 0
h_Tail= 0
h_Payload= 1.7 #[m]


#Basic cg calculations
def CG calculations(M_Fuselage, M_Landinggear, M_Prop, Props, M_Wing, M_Tail, M_Payload, h_Landinggear, h_Fuselage, h_Prop, h_Wing, h_Tail, h_Payload)
  M_Total=M_Fuselage+M_Landinggear+M_Prop*Props+M_Wing+M_Tail+M_Payload
  print('The total mass in [kg] is:', M_Total)

  cg_Landinggear= h_Landinggear/3
  cg_Fuselage= h_Landinggear+h_Fuselage/2
  cg_Prop= h_Landinggear
  cg_Wing= 0
  cg_Tail= 0
  cg_Payload= h_Landinggear+h_Payload/4

  cg_total=(M_Fuselage*cg_Fuselage+M_Landinggear*cg_Landinggear+M_Prop*cg_Prop*Props+M_Wing*cg_Wing+M_Tail*cg_Tail+M_Payload*cg_Payload)/M_Total
  print('The CG is located at a height of [m]:', cg_Total)
  return M_total, cg_Total

