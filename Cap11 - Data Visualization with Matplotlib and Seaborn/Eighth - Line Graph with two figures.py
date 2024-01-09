import matplotlib.pyplot as plt
from pylab import *

#Datas
x = linspace(0,5,10)
y1 = x ** 2
y2 = x**0.5

figure  = plt.figure()

axesOne  = figure.add_axes([0.14,0.14,0.8,0.8])
axesTwo  = figure.add_axes([0.2,0.5,0.4,0.3])

#Main figure
axesOne.plot(x,y1,'-.','r')
axesOne.set_xlabel('Years')
axesOne.set_ylabel('Humans')
axesOne.set_title('Main figure')

#Secondary figure
axesTwo.plot(x,y2,'g')
axesTwo.set_title('Secondary figure')

plt.show()