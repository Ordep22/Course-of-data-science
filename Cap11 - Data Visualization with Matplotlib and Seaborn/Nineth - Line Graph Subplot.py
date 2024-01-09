from pylab import *
from matplotlib import pyplot as plt


x = linspace(0,5,10)
yOne  = x ** 2
yTwo  = x ** 0.5

figure, axes  = plt.subplots(nrows = 1, ncols = 2)

#for ax in axes:
axes[0].plot(x,yTwo,'.-')
axes[0].set_xlabel('time(s)')
axes[0].set_ylabel('K-1')
axes[0].set_title("Deformation for 80 ºC")

axes[1].plot(x,yOne,'.-')
axes[1].set_xlabel('time(s)')
axes[1].set_title("Deformation for 200 ºC")

figure.tight_layout()
plt.show()



