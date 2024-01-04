import pandas as pd
from matplotlib import  pyplot as plt
axes  = [1,2,3,4,5]
varOne  = [25,-25,50,-5,10]
varTow = [20,-20,40,-1,11]
varThree = [13,100,15,16,33]
plt.stackplot(axes,varOne,varTow,varThree,colors= ['purple','grey','green'])
plt.show()