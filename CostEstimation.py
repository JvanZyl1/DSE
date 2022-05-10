import numpy as np
from inputs import *
from MassEstimation import *


def total_costs(W_struct, E_total, P_TOL, R_prop):
    V_H = (1/0.51)*V_cr
    CPI = 1.27 + (1.27 / 10)*(yop - 2022)
    QDF = 0.95**(1.4427*np.log(N_ps))  # Learning curve / quantity discount
    W_struct = 2.20462262 * W_struct
    P_TOL = 0.00134102209 * P_TOL  # Convert from W to hp
    R_prop = 3.2808399 * R_prop  # Convert from m to ft
    E_total = E_total / 1000  # Convert from Wh to kWh

    # Development / production costs
    C_eng = 0.083 * W_struct**0.791 * V_H**1.521 * N_ps**0.183 * 1.6 * 1.66 * 92 * CPI * ex_rate / N_ps                        # Engineering https://www.researchgate.net/profile/Falk-Goetten/publication/337757069_Cost_Estimation_Methods_for_Hybrid-Electric_General_Aviation_Aircraft/links/5de87703299bf10bc3405695/Cost-Estimation-Methods-for-Hybrid-Electric-General-Aviation-Aircraft.pdf
    C_bat = E_total * (132-(132-73)/(yop-2022)) * QDF * ex_rate                                                         # Batteries, TODO: reduction in cost per kwh
    C_motor = 174 * P_TOL * CPI * QDF * ex_rate                                                                         # Motors, TODO: check if this is similar to current motors.
    C_pms = 150 * P_TOL * CPI * QDF * ex_rate                                                                           # Power management system, plusminus 80% of motor costs.
    C_prop = 210 * N_prop * CPI * (R_prop*2)**2 * (P_TOL/(N_prop*(R_prop*2)))**0.12 * QDF * ex_rate                     # Propellers
    C_mat = 24.896 * W_struct**0.689 * V_H**0.624 * N_ps**0.792 * CPI * 1.05 * 1.33 * QDF * ex_rate / N_ps                     # Materials
    C_tool = 2.1036 * W_struct**0.764 * V_H**0.899 * N_ps**0.178 * N_psm**0.066 * 2 * 1.1 * 61 * CPI * QDF * ex_rate / N_ps    # Tooling
    C_mfg = 20.2588 * W_struct**0.74 * V_H**0.543 * N_ps**0.524 * 1.25 * 1.1 * 53 * CPI * QDF * ex_rate / N_ps                 # Manufacturing
    C_ds = 0.06458 * W_struct**0.873 * V_H**1.89 * N_proto**0.346 * CPI * 1.5 * 1.05 * ex_rate / N_ps                          # Development support
    C_fto = 0.009646 * W_struct**1.16 * V_H**1.3718 * N_proto**1.281 * CPI * 1.5 * ex_rate / N_ps                              # Flight testing operations
    C_qc = 0.13 * C_mfg * 1.5 * 1.5 * ex_rate / N_ps                                                                           # Quality control
    C_av = 15000 * CPI * QDF * ex_rate                                                                                  # Avionics
    C_lg = -7500 * CPI * ex_rate                                                                                        # Landing gear, non-retracted so saving costs
    C_pl = 0.2 * (C_bat + C_motor + C_pms + C_prop + C_mat + C_tool + C_mfg + C_qc + C_av + C_lg)                       # Product liability

    C_unit = C_bat + C_motor + C_pms + C_prop + C_mat + \
              C_tool + C_mfg + C_qc + C_av + C_lg + C_pl                                                                # Total development / production costs

    C_overhead = C_eng + C_ds + C_fto

    C_list = np.array([["UNIT COSTS", ""],
                       ["Battery costs: ", C_bat],
                       ["Motor costs: ", C_motor],
                       ["Power management system costs: ", C_pms],
                       ["Propeller costs: ", C_prop],
                       ["Material costs: ", C_mat],
                       ["Tooling costs: ", C_tool],
                       ["Manufacturing costs: ", C_mfg],
                       ["Quality control costs: ", C_qc],
                       ["Avionics costs: ", C_av],
                       ["Product liability costs: ", C_pl],
                       ["OVERHEAD COSTS", ""],
                       ["Engineering costs: ", C_eng],
                       ["Development support costs: ", C_ds],
                       ["Flight test operating costs: ", C_fto]])

    # Operating costs
    # C_ch = elec_cost * E_total / 0.85
    # C_mt = 60 * 0.3 * (h_TO / V_to + 20 / V_cruise)

    return C_unit, C_overhead, C_list



