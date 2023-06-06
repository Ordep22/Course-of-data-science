''''
[EN]

Packages and Modules

In Python, a module is a file (script) that contains Python code and can be
imported in another Python file. It is implemented to share functions, classes,
and variables between files.

A package is a collection of modules organized in a directory structure.
It permits the division of an application into multiple modules, which facilitates
maintenance and development.

'''
#Import a package in Python
import math
import random


print("The methods available in the package Math is:\n ")
print(dir(math))
print("'\n")

#Import a module from the package
#It's simple to understade the methode, from a module we can impor a package
from math import  sqrt

print(f"The square route of 25 is:{sqrt(25)} ")
print("\n")

#If you does't understand what is functionalit of the function you can use the
#The module help()
#print(help(math.sqrt(25)))

list = ["Grape","Apple","Banana"]

fruit  = random.choice(list)

print(f"The fruit selected was: {fruit}")









