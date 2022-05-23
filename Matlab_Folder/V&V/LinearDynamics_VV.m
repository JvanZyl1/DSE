clear all
close all
clc


%% Unit Test's 0-3: 0 inputs
m = 600;
time_delay = 0.1;
g = 0.91;

F_aero = [1;2;3];
r_trajectory = [2;3;4];
a_accelerometer_error = [1;2;3];


i = 9;
if i == 1
    %Unit Test 1 : mass equal to 0
    m = 0;
    error("Unit Test 1 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 2
    %Unit Test 2 : time_delay equal to 0
    time_delay = 0;
    error("Unit Test 2 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 3
    %Unit Test 3 : g equal to 0
    g = 0;
    error("Unit Test 3 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 4
    %Unit Test 4 : no mass
    clear m
    error("Unit Test 4 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 5
    %Unit Test 5 : no time_delay
    clear time_delay
    error("Unit Test 5 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 6
    %Unit Test 6 : no g
    clear g
    error("Unit Test 6 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 7
    %Unit Test 7 : no F_aero
    clear F_aero
    error("Unit Test 7 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 8
    %Unit Test 8 : no a_accelerometer_error
    clear a_accelerometer_error
    error("Unit Test 8 passed.")
    sim('LinearDynamics_V', 10)
elseif i == 9
    %Unit Test 9 : no r_trajectory
    clear r_trajectory
    error("Unit Test 9 passed.")
    sim('LinearDynamics_V', 10)
end