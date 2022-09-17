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
    return -float(gam)


step = 5.0
point = 37130.0
former = -calculate(point)
dec_rate = 0.8


while abs(step) > 0.00001:
    if point + step <= 36000.0:
        step = step * dec_rate
    if point + step > 38000.0:
        step = step * dec_rate
    point = point + step
    next_r = -calculate(point)
    if next_r < former:
        step = step * (-dec_rate)
    former = next_r
    print("point:" + str(point))
    print("former:" + str(former))
    print("step:" + str(step))

print(' ')
print("best_point:" + str(point))
print("best_p:" + str(former))




