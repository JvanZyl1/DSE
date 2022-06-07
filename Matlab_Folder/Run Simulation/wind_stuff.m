function [u0, u1, u2] = wind_stuff(u_0, u_1, u_2, xdata, ydata, zdata, xpos, ypos, zpos)

x = xdata;
y = ydata;
z = zdata;

% z = m*y + c
x_p = xpos;
y_p = ypos;
z_p = zpos;
m = (abs(max(z)) + abs(min(z)))/(abs(max(y)) + abs(min(y)));
c = z(10) - m*y(10);
c_2 = z_p + m*y_p;
y_new = (c_2 - c)/(2*m);
z_new = m*y_new + c;

[~,~,idx]=unique(round(abs(z-z_new)),'stable');
minVal = z(idx==1);
z_val = minVal(1);
u0 = u_0(z_val);
u1 = u_1(z_val);
u2 = u_2(z_val);
end