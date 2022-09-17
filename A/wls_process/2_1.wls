Clear["Global`*"];
gamma0 = Import["D:\\GitHub\\Mathematical_Modeling\\A\\transfer_data\\statics.txt"];
gamma0 = ToExpression[gamma0];
m1 = 4866;
m2 = 2433;
mm = 1165.992;
k = 80000;
g = 9.8;
rou = 1025;
r = 1;
l0 = 0.5;
h2 = 0.8;
f = 4890;
omega = 2.2143;
gamma1 = 167.8395;
x0 = -2;
xx0 = -0.29804;
eq1 = m2*(xx''[t] + x''[t]) + gamma0*xx'[t] + k*(xx[t] - xx0) == 0;
eq2 = (m1 + mm)*x''[t] + gamma1*x'[t] - k*(xx[t] - xx0) + 
    Pi*rou*g*r*r*(x[t] - x0) - f*Cos[omega*t] - gamma0*xx'[t] == 0;
sol = NDSolve[{eq1, eq2, x[0] == x0, x'[0] == 0, xx[0] == xx0, 
    xx'[0] == 0}, {x[t], xx[t]}, {t, 0, 200}];
q[t_] = sol[[1, 2]][[2]];
p = NIntegrate[gamma0*q'[t]^2, {t, 58.125, 200}]/(141.875);
Export["D:\\GitHub\\Mathematical_Modeling\\A\\transfer_data\\outputp.txt", {p}];