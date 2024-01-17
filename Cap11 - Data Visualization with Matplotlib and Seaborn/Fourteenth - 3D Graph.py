import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import pyplot as plt
from pylab import*

alpha  = 0.7
phi_ext = 2*np.pi*0.5

#Function to color map
def ColorMap (phi_m, phi_p):
    return (+ alpha - 2 * np.cos(phi_m)*cos(phi_m)-alpha*np.cos(phi_ext - 2*phi_p))

#some new datas
phi_m = np.linspace(0,2*np.pi,100)
phi_p = np.linspace(0, 2*np.pi,100)
x,y = np.meshgrid(phi_p,phi_m)
z = ColorMap(x,y).T

fig = plt.figure(figsize=(16,6))
#first graph
ax = fig.add_subplot(1,3,1, projection = '3d')
#p = ax.plot_surface(x,y,z,rstride=4,cstride=4, linewidth = 0)
p = ax.plot_surface(x,y,z,rcount = 50,ccount = 50, linewidth = 0)

#Second Graph
ax = fig.add_subplot(1,3,2, projection = '3d')
p = ax.plot_surface(x,y,z,rstride=1,cstride=1,linewidth = 0,cmap = cm.coolwarm, antialiased = False)

#Threeth Graph
ax = fig.add_subplot(1,3,3, projection  = '3d')
p = ax.plot_wireframe(x,y,z,rstride=5,cstride=5)

cb = fig.colorbar(p,shrink = 0.5)

plt.show()



