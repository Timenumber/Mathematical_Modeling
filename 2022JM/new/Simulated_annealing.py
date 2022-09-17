import subprocess
import matplotlib.pylab as plt

inp="D:/study/USTC/2022JM/statics.txt"
out="D:/study/USTC/2022JM/outputp.txt"

def calculate(r):
    with open(inp,'w') as f:
        f.write(str(r))
        f.close()
    try:
        subprocess.check_output(['wolframscript','-file','D:/study/USTC/2022JM/1_p_gamma.wls'])
    except subprocess.CalledProcessError:
        pass
    with open(out,'r') as f:
        gam=f.read()
        f.close()
    return gam


from sko.SA import SA, SAFast

s = SAFast(func=calculate, x0=0, T_max=1, T_min=1e-9, q=0.99, L=300, max_stay_counter=150, lb=0, ub=10000)

best_r, best_p = sa.run()

print('best_r:', best_r, 'best_p', best_p)


