% Values
SF = 1.5;
n_ult = 2;

C_D_beam = 1.;

% Initial / iterating values
lengths = [1.46, 1.84, 1.84, 1.84];
thicknesses = [0.003, 0.004, 0.005, 0.006];
r_init = 0.2;

% Lift assignment
%Vertical_max = Load(MTOW * g * n_ult * SF, 0, 0, 0);
%Landing = Load(0, 0, MTOW * g * n_ult * SF, 0);
%Ground = Load(0, 0, 0, 0);
%Gust = Load(MTOW*g*SF, 21, 0, 0);

% Materials
aluminium = Material(444e6, 400e6, 70e9, 283e6, 2.8e3, 26.9e9, 0);
steel = Material(570e6,240e6, 197e9, 440e6, 8.0e3, 0, 0);
titanium = Material(620e6, 880e6, 113e9, 550e6, 4.43e3, 0, 0);
carbon = Material(4274e6, 4274e6, 234e9, 55e6, 691.7, 0, 0);

% Gear
%gear1 = Gear(aluminium, 0.1, 0.05, 0.01);

% Input beam
%use_material = aluminium;
%use_beam = gear1;
%use_loadcase = Landing;


