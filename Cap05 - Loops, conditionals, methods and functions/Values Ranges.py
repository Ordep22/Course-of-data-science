"""
[EN]
The range type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in for loops.
range(start, stop[, step])
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)

[PT]
"""

#Printing values implemeting range function

##Positive numbers
for i in range(0,100,20):
    print(i)

##Negative numbers
for i in range(100,0,-20):
    print(i)

##Range in a list
lista  = ["Pedro", "Maria", "João"]
for i in range(0,len(lista)):
    print(i)


