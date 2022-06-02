function [Ang_acc] = angular_acc(W_m, W_b, B, R)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
Torque = W_m * 10 - 12;  % From literature
MOI = (1/3) * B * W_b * R^2;

Ang_acc = Torque / MOI;
%fprintf('Torque = %f [Nm]', Torque)
end