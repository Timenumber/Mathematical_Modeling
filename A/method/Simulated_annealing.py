import subprocess
import matplotlib.pylab as plt
import torch
from sko.SA import SA, SAFast
import matplotlib.pyplot as plt
import pandas as pd
import time


inp = "../transfer_data/statics.txt"
out = "../transfer_data/outputp.txt"


def calculate(r):
    start = time.time()
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
    print('r:', r)
    print('gam:', gam)
    print(' ')
    end = time.time()
    print(str((end-start)*1000)+'ms')
    return -float(gam)


# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

sa = SAFast(func=calculate, x0=[0], T_max=1, T_min=1e-9, L=10, max_stay_counter=10, lb=0, ub=10000)
# sa.to(torch.device("cuda"))
best_r, best_p = sa.run()

print('best_r:', best_r, 'best_p', best_p)

plt.plot(pd.DataFrame(sa.best_y_history).cummin(axis=0))
plt.show()