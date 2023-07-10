import os
import numpy as np
import matplotlib.pyplot as plt

file  = os.path.join("dataset.csv")

#in numpy we can criate most tipes of arrays, but, this ones will be to the same type
array  = np.loadtxt(file,delimiter= ',', usecols=(1,2),skiprows=1)

print(f"The values in the Txt file are :{array}\n")

#If you wanna this values in separate arrays you can divide this in two one.

arrayOne, arrayTwo  = np.loadtxt(file,delimiter=',',usecols=(1,2),skiprows= 1,unpack= True)

print(f"The values in the arrayOne are :{arrayOne}\n")

print(f"The values in the arraytwo are :{arrayTwo}\n")

plt.plot(arrayOne,'o',markersize = 6, color  = 'red')

plt.plot(arrayTwo,'o',markersize = 6, color  = 'green')

plt.show()








