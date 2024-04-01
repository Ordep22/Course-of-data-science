from pylab import*
from matplotlib import pyplot as plt
from random import*

x = linspace(1.5,10,50)
y = x**3

fig, axes = plt.subplots(1,4, figsize = (15,6))

axes[0].scatter(x,x+0.5*randn(len(x)), color  = "black")
axes[0].set_title("Scater Plot")
axes[0].grid(True)

axes[1].step(x,x+0.5*randn(len(x)),lw = 2, color  = "Green")
axes[1].set_title("Step Plot")
axes[1].grid(True)

axes[2].bar(x,x+0.5*randn(len(x)), color  = "Red")
axes[2].set_title("Bar Plot")
axes[2].grid(True)

axes[3].fill_between(x,x+0.5*randn(len(x)), color  = "Purple")
axes[3].set_title("Fill Between Plot")
axes[3].grid(True)

plt.show()