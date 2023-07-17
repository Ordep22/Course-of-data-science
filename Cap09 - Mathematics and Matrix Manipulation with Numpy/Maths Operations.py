import numpy as np


arrayOne = np.arange(1,10,1)

arrayTow = np.arange(1,2,10)

print(f"The array one is: {arrayOne}")

print(f"The array two is: {arrayOne}")

#Sum elements in the array

sum = arrayOne.sum()

print(f"The sum´s elements are: {sum}")

product  = np.product(arrayOne)

print(f"The product´s elements are: {product}")

cumsum  = arrayOne.cumsum()

print(f"The accumulated sum´s elements are: {cumsum}")

sumBettwem = np.add(arrayOne,arrayTow)

print(f"The sum bettwem two elements are: {sumBettwem}")






