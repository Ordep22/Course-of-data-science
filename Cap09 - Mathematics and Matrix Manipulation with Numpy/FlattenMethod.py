"""
[PT-BR]

O método flatten() com Numpy é usado para criar uma cópia unidimensional
(ou 'achatada') de um array multidimencional. Isso significa que o métoso
cria um novo array unidmencional, que contem os elementos do array multidimencional,
mas que está organizados em uma única linha. Aorden dos elementos no novo array
unidimencional segue a orden dos elementos no array multimencional


'C' significa achatar na ordem de linha maior (estilo C). 'F' significa achatar
na ordem de coluna maior (estilo Fortran-). 'A' significa achatar na ordem principal
da coluna se a for Fortran contíguo na memória, caso contrário, na ordem principal
da linha. 'K' significa achatar a na ordem em que os elementos ocorrem na memória.
O padrão é 'C'.


[EN]

The flatten() method with Numpy is used to create a one-dimensional copy
(or 'flattened') of a multidimensional array. This means that the method
creates a new unidimensional array, which contains the elements of the multidimensional array,
but which is arranged in a single line. Order of elements in the new array
one-dimensional follows the order of the elements in the multi-dimensional array.

‘C’ means to flatten in row-major (C-style) order. ‘F’ means to flatten in column-major (Fortran- style) order.
‘A’ means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise.
‘K’ means to flatten a in the order the elements occur in memory. The default is ‘C’.

"""

import  numpy as np

arrayOne  = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(f"The array one is: \n{arrayOne}\n")

print(f"The flationed array is: {arrayOne.flatten('C')}\n")

print(f"The flationed array is: {arrayOne.flatten('F')}\n")

print(f"The flationed array is: {arrayOne.flatten('A')}\n")

print(f"The flationed array is: {arrayOne.flatten('K')}\n")

















