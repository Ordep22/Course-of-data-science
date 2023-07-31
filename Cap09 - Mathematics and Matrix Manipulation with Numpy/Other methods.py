import numpy as np

#Repeat with elements in the array n times

arrayOne = np.array([1,2,3,4])

print(f"The array one is : {arrayOne}")

print(f"Reapeat with lements in the array {np.repeat(arrayOne,3)}")

#Copy the elements in the array n time with method '.tile'

print(f"Copy all lements in the array n time: {np.tile(arrayOne,2)}")

#If we can copy all elements in the array, we can use the method '.copy()'

arrayTow = np.copy(arrayOne)

print(f"Result of the mehotd copy is: {arrayTow}")

