% Efficiencies
eta_prop = 0.8 ; % efficiencies, values taken from https://arc.aiaa.org/doi/pdf/10.2514/6.2021-3169
eta_motor = 0.95 ;
eta_power_transfer = 0.97 ;
eta_battery = 0.95 ;
eta_final = eta_battery * eta_prop * eta_motor * eta_power_transfer ;
eta_E = 200      ;   % energy density of the battery in [Wh/kg] 
vol_dens = 450 ;  % volumetric energy density [Wh/L]
nu_discharge = 0.8 ;  % discharge ratio of the battery for optimal lifetime
PowWtRat = 7000    ; % power to weight ratio for the motor [W/kg]
g = 9.81          ;  % gravitional acceleration [m/s2]
redundancy_factor = 0.75   ; %here because of shitty requirement


l = 2.1 ;
D = 1.0 ;
V_cr =  180 / 3.6 ; % Cruise velocity [m/s]
N_prop = 8 ; % Number of propellers [-]
R_prop = 1.2 ; % Propeller radius [m]
A_disk = R_prop^2 * pi * N_prop ;
B_prop = 3 ; % Number of blades per propeller [-]
C_prop = 0.2;
R_hub = 0.10;
S_body = 19.24 ; % Assume fuselage to be an ellipse of revolution and calculate its wetted area
l_t = l ;
S_nac = 0 ;
N_nac = 0 ;
W_PL = 250 ; % mass of the payload in kilograms [kg]
R_pyl = 0.05 ;  % Pylon radius (assumed circular) [m]
l_pyl = 0.2  ;% Pylon length [m]
CY = 0.6 ; % Assumed fuselage side drag coefficient
S_side = 19.24 ; % Side fuselage area (ellipse) [m^2]
Side_CD_times_S = 2.67;
Front_CD_times_S = 1.16;
% Parameters for in-plane control propellers
R_cont = 0.2 ;
N_cont = 3 ;
B_cont = 5 ;
A_disk_cont = R_cont^2 * pi * N_cont;

% Airfoil NACA 23012
Cl_slope = 6; % rad^-1, for NACA 23012 airfoil
alpha_min = -10;
alpha_stall = 15;

% Configuration
x_cg = 2.7;  % From back of design box (6x5x2 m)
y_cg = 2.5;  % Middle of the design box
prop_clearance = 0.2;  % Distance between blade tips of neighbouring propellers


% Cost inputs
yop = 2025  ;            % Year of the start of production is expected
% CPI_now = 1.27;          % 1 dollar in 2012 (date of literature) is worth as much as 1.27 now, found in https://www.bls.gov/data/inflation_calculator.htm
ex_rate = 0.90   ;       % Exchange rate dollar -> euro = 0.90
% cost_per_motor = 5500 ;   % €, estimate on price of an Emrax motor (used for other power estimations as well)
N_ps = 750    ;          % Estimation of product series over 5 years
N_psm = N_ps/(12*5) ;              % Estimation of product series over 1 month
N_proto = 5       ;      % Estimation of number of prototypes created for testing purposes

% Motor inputs
%av_power = 20000 ;
%max_power = 60000 ; % W
%omega_prop = 1000 * 2 * pi / 60 ; % Rotational velocity of propeller [rad/s]
%omega_max = 6500 * 2 * pi / 60  ;

% Mission profile characteristics
R = 20000      ;     % mission range in meters [m]
R_div = 4000    ;    % additional diversion range in meters [m]
V_TO = 5         ;   % assumed take-off and descent velocity [m/s !]
h_TO = 450        ;  % assumed vertical travel distance in [m]
rho = 1.225        ; % air density in [kg/m3]
n_ult = 2           ;% ultimate load factor

% Wind speed
V_wind_avg = 21  ; %[m/s], average wind speed at 8 beaufort
dist_force = 1200   ; %[N], force expected to be experienced by side gusts

%battery stuff
Voltage = 723;   %[V]
Cell_amp = 20;   %[A]
Cell_volt = 3.6;    %[V]
CellToPack = 1.42;
En_Dens_vol = 450;   %[Wh/L]
Cell_mass = 0.0455;  %[kg]
Cell_capa = 10.8;    %[Wh]


