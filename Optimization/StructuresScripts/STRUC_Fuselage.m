%% Internal Loads and Bending Moment

%Fuselage span
x = 0:0.1:5; % [m]
loaddist = load(x);


% Load Distribution (Not correct equation)
function V = load(pos_x)
V = pos_x.^2;
end




