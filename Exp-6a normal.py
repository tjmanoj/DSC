import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import pandas as pd
d=pd.read_csv("diabetes_pima.csv")
print(d.columns)
c=str(input("Enter column name to plot normal:"))
# Plot between -10 and 10 with .001 steps.
# Calculating mean and standard deviation
m = statistics.mean(d[c])
sd = statistics.stdev(d[c])
a=np.arange(-10,10,0.001)
plt.plot(a, norm.pdf(a, m, sd))
plt.show()
