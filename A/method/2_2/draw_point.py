import subprocess
import matplotlib.pylab as plt
import pandas as pd

inp1 = "../../transfer_data/statics1.txt"
inp2 = "../../transfer_data/statics2.txt"
out = "../../transfer_data/outputp.txt"


def calculate(gamma, r):
    with open(inp1, 'w') as f:
        f.write(str(gamma))
        f.close()

    with open(inp2, 'w') as f:
        f.write(str(r))
        f.close()

    try:
        subprocess.check_output(['wolframscript', '-file', '../../wls_process/2_2.wls'])
    except subprocess.CalledProcessError:
        pass

    with open(out, 'r') as f:
        out_p = f.read()
        f.close()
    return out_p


gamma = []
r = []
p = []
circ_gamma = list(range(0, 10000, 1000))
circ_r = [i/100.0 for i in range(100)]

for i in circ_gamma:
    for j in circ_r:
        gamma.append(i)
        r.append(j)
        tmp = calculate(i, j)
        p.append(tmp)
        print("gamma:" + str(i))
        print("r:" + str(j))
        print(tmp)

data = {"gamma": gamma,
        "r": r,
        "p": p}
data = pd.DataFrame(data)
data.to_csv('../../data/data2_2.csv')

# plt.scatter(gamma, p , c=p, cmap=plt.cm.Greens, edgecolors='none', s=1)
# plt.show()