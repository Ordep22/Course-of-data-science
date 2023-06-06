''''
#Function Reduce

[PT]
A função reduce() em Python é uma função da biblioteca functools que
aplica uma determinada função binária  a pares consecutivos
de elementos em uma estrutura de dados iterável (como uma lista, tupla
ou outro objeto iterável), reduzindo-o a uma único valor.



[EN]
The reduce() function in Python is a function from the functools library that
applies a given binary function to consecutive pairs
of elements in an iterable data structure (such as a list, tuple
or other iterable object), assigns it to a single value.
'''

#Importe the function reduce from module functools
from functools import reduce

#Criete a new list
list  = [47,11,42,13]

print(list)

#Criete a new function

def sum(a,b):
    c = a + b
    return c


#Use the function reduce  to reduce the list
result = reduce(sum,list)

#Show the result
print(f"Reduce resulte: {result}")


#Anothe way to implement the function reduce is
#Implent a function lambda

list_1  = [47,11,42,13]

rl = reduce(lambda x,y:x+y,list_1)

print(f"The resulte of implementation with REDUCE and LAMBDA is:")
print(f"Reduce resulte: {rl }")

#We can assingn  a expression lambda to a variabel

list_2  = [47,11,42,13]

max_find = lambda a,b: a  if (a < b) else b

type(max_find)

res = reduce(max_find,list_2)

print(f"The resulte of implementation with REDUCE and LAMBDA as a variable:")
print(f"Reduce resulte: {res}")





















