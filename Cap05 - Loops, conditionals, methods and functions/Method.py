"""
[EN]
Method
Everything is created in Python is considered an object.
Each object have a methods and attributes

• Attributes are properties, cracristics of the object.
• Methods are functions with actions which can be executed on objects


"""
from builtins import len

# Criate a new list
lista  = [100,-2,12,65,0]

typeList = str(type(lista))

print(f"O tipo do objeto é: {typeList[8:12]}")


#Verif the object methods and atribuits
#The object list have this methods

#Add a new element
lista.append(100)


'''
lista.append()
lista.count()
lista.extend()
lista.index()
'''
#Show object list
print(lista)

#Show how methods are possible to implement in this object
print(lista.__dir__())


