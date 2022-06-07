clear all
close all
clc

a = csvread('data.csv', 1, 1);
u_0 = a(:,1);
u_1 = a(:,2);
u_2 = a(:,3);
x = a(:,4);
y = a(:,5);
z = a(:,6);

% Transform: pi/2 around Z, then pi around x

Tzy_Shard = [cos(pi/2) -sin(pi/2) 0; sin(pi/2) cos(pi/2) 0; 0 0 1]*[1 0 0;
    0 cos(pi) -sin(pi);
    0 sin(pi) cos(pi)];

r_shard = [];
P = [];
P_1 = [];
P_2 = [];
for i = 1:1:height(x)
    rshard_vec = [x(i,1); y(i,1); z(i,1)];
    rshard_rot = Tzy_Shard*rshard_vec;
    rstrans = rshard_rot.';
    r_shard = [r_shard; rstrans];
    P_add = [rshard_rot(1), rshard_rot(3), u_0(i,1)];
    P = [P; P_add];
    P_add1 = [rshard_rot(1), rshard_rot(3), u_1(i,1)];
    P_1 = [P_1; P_add1];
    P_add2 = [rshard_rot(1), rshard_rot(3), u_2(i,1)];
    P_2 = [P_2; P_add2];
end

%{
%% U_0 interpolate
x = P(:,1) ; y = P(:,2) ; z = P(:,3);
x1 = x; y1 = y; z1 = z;
ti_x = min(x):1:max(x);
ti_z = min(z):1:max(z);
[XI_u0, YI_u0] = meshgrid(ti_x,ti_z);
model_u0 = scatteredInterpolant(x, y, z, 'linear', 'linear');
ZI_u0 = model_u0(XI_u0, YI_u0);

fig1 = figure(1);
surf(XI_u0,YI_u0,ZI_u0); shading interp; hold on
colorbar
hold off
zlabel('$U_0$', 'Interpreter','Latex');
xlabel('x-position', 'Interpreter','Latex');
ylabel('z-position', 'Interpreter','Latex');
%}


%% U_1 interpolate
x = P_1(:,1) ; y = P_1(:,2) ; z = u_1;
x1 = x; y1 = y; z1 = z;
ti_z = -240:1:-160;
ti_y = -125:1:174;
[XI_u1, YI_u1] = meshgrid(ti_y,ti_z);
model_u1 = scatteredInterpolant(x, y, z, 'linear', 'linear');
ZI_u1 = model_u1(XI_u1, YI_u1);

fig2 = figure(2)
surf(XI_u1,YI_u1,ZI_u1); shading interp; hold on
colorbar
hold off
zlabel('$U_1$', 'Interpreter','Latex');
xlabel('y-position', 'Interpreter','Latex');
ylabel('z-position', 'Interpreter','Latex');

%{
%% U_2 interpolate
x = P_2(:,1) ; y = P_2(:,2) ; z = P_2(:,3) ;
x1 = x; y1 = y; z1 = z;
ti = -250:1:250;
[XI_u2, YI_u2] = meshgrid(ti,ti);
model_u2 = scatteredInterpolant(x, y, z, 'linear', 'linear');
ZI_u2 = model_u2(XI_u2, YI_u2);

fig3 = figure(3)
surf(XI_u2,YI_u2,ZI_u2); shading interp; hold on
colorbar
hold off
zlabel('$U_2$', 'Interpreter','Latex');
xlabel('y-position', 'Interpreter','Latex');
ylabel('z-position', 'Interpreter','Latex');


%}

