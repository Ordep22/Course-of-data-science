from matplotlib import  pyplot as plt
import numpy as np


data  = np.random.randn(10000)

fig, axes  = plt.subplots(1,2,figsize = (10,4))


axes[0].hist(data)
axes[0].set_title("Standard Histogram")
axes[0].set_xlim(min(data),max(data))

axes[1].hist(data, cumulative = True, bins = 50)
axes[1].set_title("Cumulative Histogram")
axes[1].set_xlim(min(data),max(data))

plt.show()
