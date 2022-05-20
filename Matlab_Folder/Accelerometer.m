%
% Create gyroscope sensor object
params = accelparams 

% Parameters for simulated signal
N = 1000;       % Number of samples
Fs = 100;       % Sampling rate
Fc = 0.25;      % Sinusoidal frequency


% Create arrays
t = (0:(1/Fs):((N-1)/Fs)).';
acc = zeros(N, 3);          %Input accelerations
orient = quaternion.ones(N, 1);
angvel = zeros(N, 3);

% Generate acceleration data
imu = imuSensor('SampleRate', Fs, 'Accelerometer', params);
imu.Accelerometer.MeasurementRange = 10;   % Maximum acceleration accelerometer can measure
imu.Accelerometer.Resolution = 1/Fs;           % Step size of digital measurements

% Biases
imu.Accelerometer.BiasInstability = 7.5 / 1000;
imu.Accelerometer.NoiseDensity = 150 / 1000 / 1000;
imu.Accelerometer.TemperatureBias = 50 / 1000 / 1000;


imu = imuSensor('SampleRate', Fs, 'Accelerometer', params);

accelData = imu(acc, angvel, orient);

% Plot simulated signal
figure
plot(t,accelData)
xlabel('Time (s)')
ylabel('Acceleratio (m/s^2)')
title('Ideal Acceleration Data')