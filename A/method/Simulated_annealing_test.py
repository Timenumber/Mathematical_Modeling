import subprocess
import matplotlib.pylab as plt

inp = "../transfer_data/statics.txt"
out = "../transfer_data/output.txt"


def calculate(r):
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
    return gam


gamma = []
p = []
circ = list(range(0, 10000, 100))
for i in circ:
    gamma.append(i)
    p.append(calculate(i))
    print(i)
plt.scatter(gamma, p , c=p, cmap=plt.cm.Greens, edgecolors='none', s=1)
plt.show()