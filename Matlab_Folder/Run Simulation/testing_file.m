a = csvread('data.csv', 1, 1);

d = 1001; %1002
u_0 = a(1:d,1);
u_1 = a(1:d,2);
u_2 = a(1:d,3);
x = a(1:d,4);
y = a(1:d,5);
z = a(1:d,6);

% z = m*y + c
y_p = y(5) * 1.05;
z_p = z(5) * 1.05;
m = (abs(max(z)) + abs(min(z)))/(abs(max(y)) + abs(min(y)));
c = z(10) - m*y(10);
c_2 = z_p + m*y_p;
y_new = (c_2 - c)/(2*m);
z_new = m*y_new + c;

[~,~,idx]=unique(round(abs(z-z_new)),'stable');
minVal = z(idx==1);
z_val = minVal(1);
u_val = u_0(z_val);


fig1 = figure(1)
plot3(y,z, u_0)
xlabel('y')
ylabel('z')
zlabel('u_0')

fig2 = figure(2)
plot3(y,z, u_1)

fig3 = figure(3)
plot3(y,z, u_2)