import numpy as np
from inputs import *
from MassEstimation import *
from main import P_hov

W_bat = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_hov, P_cruise, nu_discharge)
W_s = StructureMassFun(n_ult, D, l, MTOW)

def total_costs(MTOW, W_struct, E_total, P_TOL):
    V_H = (1/0.51)*V_cruise
    QDF = 0.95**(1.4427*ln(N_ps))  # Learning curve / quantity discount

    # Development / production costs
    C_eng = 0.083 * W_struct**0.791 * V_H**1.521 * N_ps**0.183 * 1.6 * 1.66 * 92 * CPI                                  # Engineering
    C_bat = E_total * cost_per_kwh * QDF                                                                                # Batteries, TODO: reduction in cost per kwh
    C_motor = 174 * P_TOL * CPI * QDF                                                                                   # Motors, TODO: check if this is similar to current motors.
    C_pms = 150 * P_TOL * CPI * QDF                                                                                     # Power management system, plusminus 80% of motor costs.
    C_prop = 210 * N_prop * CPI * (R_prop*2)**2 * (P_TOL/(N_prop*(R_prop*2)))**0.12 * QDF                               # Propellers
    C_mat = 24.896 * W_struct**0.689 * V_H**0.624 * N_ps**0.792 * CPI * 1.05 * 1.33 * QDF                               # Materials
    C_tool = 2.1036 * W_struct**0.764 * V_H**0.899 * N_ps**0.178 * N_psm**0.066 * 2 * 1.1 * 61 * CPI * QDF              # Tooling
    C_mfg = 20.2588 * W_struct**0.74 * V_H**0.543 * N_ps**0.524 * 1.25 * 1.1 * 53 * CPI * QDF                           # Manufacturing
    C_ds = 0.06458 * W_struct**0.873 * V_H**1.89 * N_proto**0.346 * CPI * 1.5 * 1.05                                    # Development support
    C_fto = 0.009646 * W_struct**1.16 * V_H**1.3718 * N_proto**1.281 * CPI * 1.5                                        # Flight testing operations
    C_qc = 0.13 * C_mfg * 1.5 * 1.5                                                                                     # Quality control
    C_av = 15000 * CPI * QDF                                                                                            # Avionics
    C_lg = -7500 * CPI                                                                                                  # Landing gear, non-retracted so saving costs
    C_pl = 0.2 * (C_bat + C_motor + C_pms + C_prop + C_mat + C_mat + C_tool + C_mfg + C_qc + C_av + C_lg)               # Product liability

    # Operating costs
    C_ch = elec_cost * E_total / 0.85
    C_mt = 60 * 0.3 * ()


