"""
LIST COMPREHENSION

[Expression for item interable if condiitional iquals true]
List comprehensions provide a concise way to create lists. Common
applications are to make new lists where each element is the result of
some operations applied to each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain condition.

"""

#List comprehension witch show the numbers until ten

listComprehension = [x for x in range(10)]

print(listComprehension)

#List comprehetion witch show the numbers smalles tham five from one to ten

listComprehension1 = [x for x in range(1,10) if x < 5]
print(listComprehension1)

#Comper the performance betwhem for and list comprehention

#For way
fruitLista  = ["Maça", "Banana", "Mamão","Abacaxi"]
newList = []

for i in fruitLista:
    if "M" in i or "M" in i:
        newList.append(i)
print(newList)

#List Comprehention way
listComprehension2 = [x for x in fruitLista if "m" in x or "M" in x]

print(listComprehension2)

"""
Well, we can see that the list comprehension method is the simplest. 
However, the for loop method has its applications and should not be excluded.
"""

"""
DICT COMPREHENSION

In addition, dict comprehensions can be used to create dictionaries from 
arbitrary key and value expressions
{x: x**2 for x in (2, 4, 6)}
"""
#Dictionary studants and notes
dictStudants  = {"Bob":68,"Michel": 84, "Zico": 57, "Ana": 93}

#Create a new dictionary with the statuses: Notes bigger than 70 (approved), else (rejected).

newDictionary = {x:y for (x,y) in dictStudants.items()}
print(newDictionary)

newDictionary = {x:("Approved" if y >= 60 else "Rejected" ) for (x,y) in dictStudants.items()}
print(newDictionary)








