from pylab import*
from matplotlib import  pyplot as plt


x = linspace(0,5,10)
y = x**2

#Creating the  subplot
fig, axes = plt.subplots(1,2,figsize = (10,4))

#Criating the first plot
axes[0].plot(x,y,x,exp(x))
axes[0].set_title("Standard Scale")

#Cirating the second plot
axes[1].plot(x,y,x,exp(x))
#It's so simple to change the graph scale, It's only add "log" in set_yscale
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic Scale (y)")


plt.show()