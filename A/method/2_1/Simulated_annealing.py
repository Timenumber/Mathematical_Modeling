import subprocess
import matplotlib.pylab as plt
import torch
from sko.SA import SA, SAFast
import matplotlib.pyplot as plt
import pandas as pd
import time


inp = "../../transfer_data/statics.txt"
out = "../../transfer_data/outputp.txt"


def calculate(r):
    r = float(r)
    with open(inp, 'w') as f:
        f.write(str(r))
        f.close()
    try:
        subprocess.check_output(['wolframscript', '-file', '../../wls_process/2_1.wls'])
    except subprocess.CalledProcessError:
        pass
    with open(out, 'r') as f:
        gam = f.read()
        f.close()
    print("r:", r)
    print("p:", gamma)
    return -float(gam)

# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

sa = SA(func=calculate, x0=[0], T_max=1, T_min=1e-9, L=10, max_stay_counter=10, lb=36000, ub=38000)
# sa.to(torch.device("cuda"))
best_r, best_p = sa.run()

print('best_r:', best_r, 'best_p', best_p)

plt.plot(pd.DataFrame(sa.best_y_history).cummin(axis=0))
plt.show()