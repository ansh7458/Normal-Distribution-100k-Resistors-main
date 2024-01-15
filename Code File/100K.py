import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm


data = pd.read_csv('jj.csv')

x=data['Value']


plt.hist(x,bins=25)

plt.xlabel("Resistor Values (kΩ)")
plt.ylabel("Frequency")


print("MAx element",max(x))

print("Min element",min(x))

plt.show()