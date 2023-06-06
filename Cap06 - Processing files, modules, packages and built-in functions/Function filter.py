#Function filter ---> Verificar se essa função filter está ativa na Python 3.8

"""
[PT]
A função filter em Python é uma função que filtra elementos de uma estrutura
de dados iterável (como uma lista, tupla ou outro objeto iterável) como base
em uma função determinada condição. A função filter() retorna um objeto filtro
que pode ser contido em outra estrutura de dados, como uma lista, se necessário.

[EN]
The filter function in Python is a function that filters elements of a structure
iterable data object (such as a list, tuple, or other iterable object) as a basis
in a given condition function. The filter() function returns a filter object
which can be contained in another data structure, such as a list, if necessary.
"""

#Create a list
oldList  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#Implementing the lambda function
newList = list(filter(lambda x: x%2 ==0,oldList))

#Show the new list
print(f"The new list is: {newList}")































