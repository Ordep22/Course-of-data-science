
tupla  = ("Nomes",2,"Strings")
print(tupla)

'''
As tuplas são elementos bastante limitados
nelas não é possível adicionar um elemento, pois, não modemos modificar sua estrutura.

'''

##Pesquisando por um indice
tupla_01 = ("Chocolate")
print(tupla_01[0])

##Percorrendo a tupla
print(tupla[0:1])

#Verificando o indice do elemento
print(tupla.index("Strings"))

#Como a tupla é imutável posemos implemtar alguma funções para manipular sua rstrição
Lista = list(tupla)
print(Lista)
Lista.append("CPF")
print(Lista)
tupla = tuple(Lista)
print(tupla)


