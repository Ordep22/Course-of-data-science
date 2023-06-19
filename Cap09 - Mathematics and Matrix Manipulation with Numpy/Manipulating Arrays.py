import numpy as np

#Criating a array
matrix  = np.array([[1,2,3],[4,5,6]])

#The type of matrix
print(type(matrix))

#Show the array content
print(matrix)

#Show the shape of matrix
print(matrix.shape)

#---------------------------------------------------------------------------------------------------------------------#

#creating a matrix just with "1"
matrixOnes = np.ones((2,3)) # => this method recive the shape of array

#Show the ones array
print(matrixOnes)


#---------------------------------------------------------------------------------------------------------------------#

#Criating a list of list
list  = [[13,81,22],[0,34,59],[21,48,94]]

#The matrix functions  criate a matrix from the list of lists
matrixTwo = np.matrix(list)

#Show de type of matrixTwo
print(type(matrixTwo))

#Show the matrixTwo
print(matrixTwo)

#Show the shape of matrixTow
print(matrixTwo.shape)

#Show the zise of matrixTwo
print(matrixTwo.size)

#Show the type of
print(matrixTwo.dtype)

#Matrix indexing
print(matrixTwo[0,1])

#Matrix indexing
print(matrixTwo[0:2,1])

#Matrix indexing
print(matrixTwo[1,]) # => Get the elements in line one

#Change the element in the expecific index
matrixTwo[0,1] = 80
print(matrixTwo)

#---------------------------------------------------------------------------------------------------------------------#

#Expecifi the type of data

x = np.array([1,2]) #Numpy will choice the type of data

print(x.dtype)

y = np.array([1.0,2.0]) #Numpy understante tha type is float

print(y.dtype)


z = np.array([1,2], dtype=np.float64) #Fix the type of Data

print(z.dtype)


#---------------------------------------------------------------------------------------------------------------------#
matrixThree = np.array([[13,81,22],[0,34,59],[21,48,94]],dtype=float)
print(matrixThree)

#Showing how many bytes each variable occupies
print(matrixThree.itemsize)

#Showing how many bytes each array occupies
print(matrixThree.nbytes)

#Showing how many dimensions the array has
print(matrixThree.ndim)









































