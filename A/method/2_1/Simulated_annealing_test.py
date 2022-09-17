import subprocess
import matplotlib.pylab as plt
import pandas as pd

inp = "../../transfer_data/statics.txt"
out = "../../transfer_data/outputp.txt"


def calculate(r):
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
    return gam


gamma = []
p = []
circ = list(range(37000, 38000, 10))
for i in circ:
    gamma.append(i)
    tmp = calculate(i)
    p.append(tmp)
    print(i)
    print(tmp)

data = {"gamma": gamma,
        "p": p}
data = pd.DataFrame(data)
data.to_csv('../../data/data2_1_precise.csv')

# plt.scatter(gamma, p , c=p, cmap=plt.cm.Greens, edgecolors='none', s=1)
# plt.show()