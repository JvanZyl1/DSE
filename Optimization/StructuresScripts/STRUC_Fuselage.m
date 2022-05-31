%% Internal Loads and Bending Moment

%Fuselage span
x = 0:0.1:5; % [m]
loaddist = load(x);
momentdist = moment(x);


%% Boom assignment

%Cross-section 1
boom1 = FL_Booms(500, 1000, 50);

boom1.xi



% Load Distribution (Not correct equation)
function V = load(pos_x)
V = pos_x.^2;
end

% Moment Distribution (Not correct equation)
function M = moment(pos_x)
M = pos_x.^2;
end


