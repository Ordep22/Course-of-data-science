'''

Loop for
valida cada item em uma série de valores

for item in série-de-itens:
    executa comandos

Podemos utilizar o loop for em objetos sequenciais como:
 - strings
 - listas
 - tuplas
 - elementos de dicionário
 - arquivos

'''


'''


##Loop while
Reservate words

break  -> Stop loop
continue    -> Continuos the interation 
pass   -> It doesn't execute this interation

'''


'''
Estrutura de repetição range

A função range() tem o seguinte formato:

range([start],[stop],[step])

[start] - número que inicia a sequência
[stop]  - número que encerra a sequência(não é incluso na sequência)
[step] - incremento da sequência



'''
#Loop for
'''
for c in range (0,10,1):
    print(c)

for d in range (10,0,-1):
    print(d)

#Criate a tuple and show in terminal your elements

tuple  = (1,2,3,4)

for i in tuple:
    print(f"O elemento da tupla é: {i}")

'''''
#Criate a list and show your elements
'''''
listStrings  = ["Data", "Science","Academi"]

for i in listStrings:
    print(i)

#Loop for nested

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in matriz:
    for y in i:
        print(y)
    print(10*"--")

'''
#Loop while

#Goes into the loop if conditional value is true
"""
value = 0
while value <= 10:
    print(value)
    value+=1
"""


#It's possible to use a clausule else for finish a loop while
"""
x = 0
while x < 10:
    print(f"The x value in this iteration is: {x}")
    x += 1
else:
    print("Loop conclused")


"""

#Pass, Break, Continue

## If find the number four the is break
''''
value  = 0
while value < 10:
    if value == 4:
        break
    else:
        pass
    print(f" {value} \n")
    value += 1
'''''
#Whem we use continue, the python interpreter simply continues the interation
'''''
for letter in "Python is ZZZ incrible":
    if letter == "Z":
        continue
    print(letter)
'''''
#While and For in the same loop
import time
primeNumbers  = []
numberVerification = []
prime = True
divider = 1
initialTime  = time.time()
for iten in range(2,30,1):

    numberVerification = []
    divider  = 1

    while (divider <= iten):

        if (iten % divider) == 0:
            numberVerification.append(True)

        divider += 1

    if numberVerification.count(True) == 2:
            primeNumbers.append(iten)
finalTime  = time.time()
print(30*"----")
print(f"Foram identificados {len(primeNumbers)} números primos")
print("\n")
print(primeNumbers)
print("\n")
print(f"Com tempo de execução igual a: {(finalTime - initialTime)} s")
print(30*"----")

























































