import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/data2_1_precise.csv")

plt.plot(data['gamma'], data['p'])

plt.savefig("2_1_precise.png")
plt.show()