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

fig = plt.figure(figsize=(14,6))
plt.show()



