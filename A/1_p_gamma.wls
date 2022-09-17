Clear[gamma0];
gamma0 = Import["C:\\Users\\HP\\Desktop\\A\\transfer_data\\statics.txt"];
gamma0 = ToExpression[gamma0];
m1 = 4866;
m2 = 2433;
mm = 1335.535;
k = 80000;
g = 9.8;
rou = 1025;
r = 1;
l0 = 0.5;
h2 = 0.8;
f = 6250;
omega = 1.4005;
gamma1 = 656.3616;
x0 = -2;
xx0 = -0.29804;
eq1 = m2*(xx''[t] + x''[t]) + gamma0*xx'[t] + k*(xx[t] - xx0) == 0;
eq2 = (m1 + mm)*x''[t] + gamma1*x'[t] - k*(xx[t] - xx0) + 
    Pi*rou*g*r*r*(x[t] - x0) - f*Cos[omega*t] - gamma0*xx'[t] == 0;
sol = NDSolve[{eq1, eq2, x[0] == x0, x'[0] == 0, xx[0] == xx0, 
    xx'[0] == 0}, {x[t], xx[t]}, {t, 0, 100}];
q[t_] = sol[[1, 2]][[2]];
p = NIntegrate[gamma0*q'[t]^2, {t, 60, 100}]/60;
Export["C:\\Users\\HP\\Desktop\\A\\transfer_data\\outputp.txt", {p}];