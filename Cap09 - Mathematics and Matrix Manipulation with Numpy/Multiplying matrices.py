"""
[PT-BR]

Para multiplicar matrizes com o Numpy, podemos usar a função '.dot()'
ou o operador @. Ambos os métodos executão a maultiplicação matricial.
É importante lembrar que, para que a multiplicação possa ser executadada,
o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.

Há várias formas de multiplicar elemtentod de matrizes Numpy. A função '.dot()'
é o métodos mais utilizado.


[EN]

To multiply matrices with Numpy, we can use the '.dot()' function
or the @ operator. Both methods perform matrix manipulation.
It is important to remember that, for the multiplication to be performed,
the number of columns in the first matrix must be equal to the number of rows in the second matrix.

There are several ways to multiply elementtentod from Numpy arrays. The '.dot()' function
is the most used method.

"""

import numpy as np


MatOne  = np.array([[1,2],[4,5]])

MatTow = np.array([[7,8,9],[10,11,12]])

print(f"The shape one is: {MatOne.shape}")

print(f"The shape tow is: {MatTow.shape}")

productResultone = np.dot(MatOne,MatTow)

print(f"The result betwem MatOne and MatTow is: {productResultone}")

#If we can implement the operator @, we can do this.

productResulttow = MatOne@MatTow

print(f"The result betwem MatOne and MatTow is: {productResulttow}")

#If we can implement the operator '.thensordot()', we can do this.


productResulthree = np.tensordot(MatOne,MatTow,axes=((1),(0)))

print(f"The result betwem MatOne and MatTow is: {productResulthree}")


#As we can see, all show methods work's the same way.
















