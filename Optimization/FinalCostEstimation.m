function [outputArg1,outputArg2] = FinalCostEstimation(inputArg1,inputArg2)
    % This function is a combination of equations of the parametric method of
    % the midterm report, and a more accurate method specifically created for
    % the final design of the vehicle. 
    % PARAMETRIC METHOD: 
    %   - Engineering
    %   - Development support
    %   - Flight testing operations
    %   - Quality control
    %   - Product liability
    %   - 
    %   - 
    %   - 
    %   - 
    % NEW METHOD: 
    %   - Motor
    %   - Power management system
    %   - Propellers
    %   - Materials
    %   - Tooling
    %   - Manufacturing
    %   - Avionics
    %   - Landing gear
    %   - 
    C_eng = 0.083 * W_struct^0.791 * V_H^1.521 * N_ps^0.183 * 1.6 * 1.66 * 92 * CPI * ex_rate;%                        # Engineering https://www.researchgate.net/profile/Falk-Goetten/publication/337757069_Cost_Estimation_Methods_for_Hybrid-Electric_General_Aviation_Aircraft/links/5de87703299bf10bc3405695/Cost-Estimation-Methods-for-Hybrid-Electric-General-Aviation-Aircraft.pdf

    C_bat = E_total * (132-(132-73)/(yop-2022)) * QDF * ex_rate;%                                                         # Batteries
    C_motor = 174 * P_TOL * CPI * QDF * ex_rate;%                            # Motors, TODO: check if this is similar to current motors.
    C_pms = 150 * P_TOL * CPI * QDF * ex_rate;%                                                                           # Power management system, plusminus 80% of motor costs.
    C_prop = 210 * N_prop * CPI * (R_prop*2)^2 * (P_TOL/(N_prop*(R_prop*2)))^0.12 * QDF * ex_rate;%                     # Propellers
    C_mat = 24.896 * W_struct^0.689 * V_H^0.624 * N_ps^0.792 * CPI * 1.05 * 1.33 * QDF * ex_rate / N_ps;%                     # Materials
    C_tool = 2.1036 * W_struct^0.764 * V_H^0.899 * N_ps^0.178 * N_psm^0.066 * 2 * 1.1 * 61 * CPI * QDF * ex_rate / N_ps;%    # Tooling
    C_mfg = 20.2588 * W_struct^0.74 * V_H^0.543 * N_ps^0.524 * 1.25 * 1.1 * 53 * CPI * QDF * ex_rate / N_ps;%                 # Manufacturing
    C_ds = 0.06458 * W_struct^0.873 * V_H^1.89 * N_proto^0.346 * CPI * 1.5 * 1.05 * ex_rate;%                          # Development support
    C_fto = 0.009646 * W_struct^1.16 * V_H^1.3718 * N_proto^1.281 * CPI * 1.5 * ex_rate;%                              # Flight testing operations
    C_qc = 0.13 * C_mfg * 1.5 * 1.5 * ex_rate / N_ps;%                                                                           # Quality control
    C_av = 15000 * CPI * QDF * ex_rate;%                                                                                  # Avionics
    C_lg = -7500 * CPI * ex_rate;%                                                                                        # Landing gear, non-retracted so saving costs
    C_pl = 0.2 * (C_bat + C_motor + C_pms + C_prop + C_mat + C_tool + C_mfg + C_qc + C_av + C_lg);%                       # Product liability

end

