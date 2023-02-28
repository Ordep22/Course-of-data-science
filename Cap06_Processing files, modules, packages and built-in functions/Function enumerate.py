''''
#Function Enumerate

[PT]
A função enumerate() em Python é uma funcão que permite iterar sobre
uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). Afunção
enumerate() retorna um objeto enumerado, que pode ser usado em loops
para percorrer a estrutura de dados e acessar o contador e o valo de cada elemento

[EN]

'''

#Create e new list\
oldList = ['a','b','c']

newList = list(enumerate(oldList))
print(newList)
print("oldLis enumerate is:")
for i ,j in newList:
    print(i, j)




