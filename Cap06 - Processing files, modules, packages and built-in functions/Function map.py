''''
#Function Map

[PT]
A função map( )  em Python é a função que aplica uma determinada função
a cada elemento de uma estrutura de dados iterável (como um lista, tupla ou
outro objto iterável ). A função map() retorna um objeto que pode ser
convertido em outra estrutura de dados, como um lista, se necssário.

[EN]
The map( ) function in Python is the function that applies a given function
to each element of an iterable data structure (such as a list, tula, or
another iterable object). The map() function returns an object that can be
converted to another data structure, such as a list, if necessary.
'''

#Function Python thats  return a square number

def SQUARENUMBER(number):
    return number**2

listNumebers = [1,2,3,4,5]

exit  = map(SQUARENUMBER,listNumebers)

suquareNumbers  = list (exit)

print(30*"---")
print(suquareNumbers)
print(30*"---")


#print(suquareNumbers)


#------------------------------------------------------------------------------------------------------------------------


#Create tow functions

#Func 1 - Receive temperature with parameter and return the parameter in Fahrenheit
def FAHRENHEIT(temperatur):
    return ((float(9)/5)*(temperatur+32))

#Func 2 - Receive temperature with parameter and return the parameter in Celsius
def CELSIUS(temperatur):
    return ((float(5)/9)*(temperatur-32))

listTempemperatur  = [0,20.5,40,100]


#Checking the result of the map function
#In Python 3, the map function returns an iterator
#Means it's an object you can walk around with
mapResult = map(FAHRENHEIT,listTempemperatur)
print(mapResult)
print(30*"---")

#Verify the resulte of map function in a list
mapResultlist = list(map(FAHRENHEIT,listTempemperatur))
print("Temperatur in Fahrenheit")
for i in mapResultlist:
    print(f"Temperatur: {i} F")

print(30*"---")

#Aply the Lambda function with map()

listImpar = [1,3,5,7]
lisPar = [2,4,6,8]

#Some tow lists

listSum = list(map(lambda x,y:x+y,listImpar,listImpar))

for j in listSum:
    print(f"x + Y =  {j}")








































