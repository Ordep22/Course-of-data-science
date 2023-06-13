import numpy as np

arrOne  = np.array([10,21,32,43,48,15,76,57,89])


#Show an expecific element in numpy array
print(f"The third element in a array is:{arrOne[3]}")

#Showing a sequence of elements starting from the initial element
print(f"The seuqneci from {arrOne[2]} to {arrOne[6]} is: {arrOne[2:7]}")

#Crating a list to index elements in the Numpy arrays

indexList = [1,3,5,7]

#Showing the elements from the list index
print(f"The elements from the list {indexList} is: {arrOne[indexList]}")


#Crating a mask with Numpy arrays
mask  = (arrOne % 2 == 0)

#show mask
print(f"The mask aplay to the list is:{mask}")

#Verifing the elements that is true whem it´s divided by two
print(f"The mask aplay to the array one is:{arrOne[mask]}")


#Alter an element in Numpy array
arrOne[0] = 100
print(f"The new element in the first position is:{arrOne[0]}")

'''
In Numpy arrays it's not  permited to change the type of varibles. 
So, the next operation it´s not permited
'''

try:
    arrOne[0] = "New element"
except:
    print("This operation it´s not permited!")
    


















