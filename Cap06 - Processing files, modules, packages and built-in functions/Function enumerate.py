''''
#Function Enumerate

[PT]
A função enumerate() em Python é uma função que permite iterar sobre
uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). A função
enumerate() retorna um objeto enumerado, que pode ser usado em loops
para percorrer a estrutura de dados e acessar o contador e o valo de cada elemento

[EN]
The enumerate() function in Python is a function that allows iterating over
a data structure (such as a list, tuple, or other iterable object). The function
enumerate() returns an enumerated object, which can be used in loops
to traverse the data structure and access the counter and value of each element
'''

#Create e new list\
oldList = ["Pedro ","Paulo","João","Amanda","Maria"]

newList = list(enumerate(oldList))
print(newList)
print("oldLis enumerate is:")
for i ,j in newList:
    print(f"{i} .>", f"{j}")





