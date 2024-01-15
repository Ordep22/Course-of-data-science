from pylab import*
from matplotlib import  pyplot as plt

x = linspace(0,5,10)
y = x**2

#Creating the  subplot
fig, axes = plt.subplots(1,4,figsize = (12,5))

#The first plot
axes[0].plot(x,y)
axes[0].set_title("Standard Scale")
axes[0].grid(True)


axes[1].plot(x,y)
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic Scale (y)")
axes[1].grid(True)


axes[2].plot(x,y)
axes[2].set_yscale("symlog")
axes[2].set_title("Symlog Scale (y)")
axes[2].grid(True)

axes[3].plot(x,y)
axes[3].set_yscale("logit")
axes[3].set_title("Logit Scale (y)")
axes[3].grid(True)

plt.show()

