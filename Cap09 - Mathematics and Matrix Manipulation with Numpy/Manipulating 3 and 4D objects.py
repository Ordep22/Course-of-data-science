import numpy as np


#Criating a 3D array

tridimentionalArray = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

#Show the number of dimentions
print(f"The number of dimentions are: {tridimentionalArray.ndim}")

#Show the shape of this array
print(f"The shape of this array are: {tridimentionalArray.shape}")

#fin an element on the array
print(f"The shape of this array are: {tridimentionalArray[0,2,2]}")

# Definindo as dimensões do array
dim1 = 2
dim2 = 3
dim3 = 4
dim4 = 5

# Gerando um array 4D com valores inteiros aleatórios entre 0 e 9
array_4d = np.random.randint(0, 10, size=(dim1, dim2, dim3, dim4))

print(array_4d)

#Show the number of dimentions
print(f"The number of dimentions are: {array_4d.ndim}")

#Show the shape of this array
print(f"The shape of this array are: {array_4d.shape}")

#fin an element on the array
print(f"The shape of this array are: {array_4d[0,2,2,2]}")


