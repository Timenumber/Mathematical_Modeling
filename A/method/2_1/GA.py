import subprocess
import matplotlib.pylab as plt
import torch
from sko.SA import SA, SAFast
from sko.GA import GA
inp = "../transfer_data/statics.txt"
out = "../transfer_data/outputp.txt"


def calculate(r):
    r = float(r)
    with open(inp, 'w') as f:
        f.write(str(r))
        f.close()
    try:
        subprocess.check_output(['wolframscript', '-file', '../1_p_gamma.wls'])
    except subprocess.CalledProcessError:
        pass
    with open(out, 'r') as f:
        gam = f.read()
        f.close()
    print(r)
    print(gam)
    return float(gam)


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

ga = GA(func=calculate, n_dim=1, lb=0, ub=10000)
ga.to(torch.device("cuda"))
best_r, best_p = ga.run()

print('best_r:', best_r, 'best_p', best_p)