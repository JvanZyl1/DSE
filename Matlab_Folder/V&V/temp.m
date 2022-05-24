%mdl = 'ampc_cstr_linearization';
%open_system(mdl)

%https://nl.mathworks.com/help/mpc/ug/adaptive-mpc-control-of-nonlinear-chemical-reactor-using-successive-linearization.html

clear all
close all
clc
I_xx = 1;
I_xy = 2;
I_xz = 1;
I_yx = 2;
I_yy = 1;
I_yz = 2;
I_zx = 3;
I_zy = 4;
I_zz = 2;

I_mat = [I_xx I_xy I_xz;
    I_yx I_yy I_yz;
    I_zx I_zy I_zz];