P = [0, 0, -1.32;
    0, 90, 0.29;
    0, 45, -1.15;
    0, 135, 1.29;
    0, 180, 1.29;
    15, 0, -1.33;
    -15, 0, -1.48;
    15, 90, 0.3;
    30, 90, 0.32;
    -15, 90, 0.32];
x = P(:,1) ; y = P(:,2) ; z = P(:,3) ;
x = [abs(x); -abs(x); abs(x); -abs(x)];
y = [abs(y);
%x = [0, 0, 0, 0, 0, 15, -15, 0, 0, 0];
%y =[0, 90, 45, 135, 180, 0, 0, 90, 90, 90];
%z = [-1.32, 0.29, -1.15, 1.29, 1.29, -1.33, -1.48, 0.3, 0.32, 0.32 ];
ti = 0:1:180;
[XI, YI] = meshgrid(ti,ti);
model = scatteredInterpolant(x, y, z, 'linear', 'linear');
ZI = model(XI, YI);
fig1 = figure(1)
surf(XI,YI,ZI); shading interp; hold on
plot3(x,y,z,'ro'); hold on
plot3(-x, y, z, 'ro') 
plot3(x, -y, z, 'ro')
plot3(-x, -y, z, 'ro')
colorbar
hold off