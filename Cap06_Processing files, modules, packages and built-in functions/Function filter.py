#Function filter ---> Verificar se essa função filter está ativa na Python 3.8



"""
[PT]
A função filter em Python é uma função que filtra elementos de uam estrutura
de dados iterável (como uma lista, tupla ou outro objeto iterável) como base
em uma função determinada condição. A função filter() retorna um objeto filtro
que pode ser conrtido em outra estrutura de dados, como uma lista, se necessário.

[EN]

"""
from fnmatch import filter


#Criate a function with verifi if the number ir pair or no

def verpair (num):
    if num % 2 == 0:
        return True
    else:
        return False


#Create new list
lista = [1,2,3,4,5,6,7,8,9,10]


#The function filter() return a interator

a = list(filter(lambda x: x%2 ==0,lista))
print(a)



























