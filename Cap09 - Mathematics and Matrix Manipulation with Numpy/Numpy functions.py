import numpy as np

#Function ARRAY
arrOne  = np.array([1,2,3,4,5,6,7,8,9])


#Use the method with Numpy
print(f"CUMSUM = {arrOne.cumsum()}")


#Function ARANGE
arrTwo  = np.arange(0,11,0.5)

print("The result of the function arrange is:")

print(arrTwo)

'''
This two functions make the same function. But 'array' you can especi the elements while 
'arange' you especifi the start, stop and increment of this range.

'''


#Function ZEROS

#Criate an array with zeros.

arrThree = np.zeros(10)

print(f"The zeros array is:{arrThree}")

#Function EYE

#Criate a diagonal matrix

arrFour  = np.eye(3) #Criate a matrix 3x3

print(f"The diagonal matrix is: \n {arrFour}")


#Diag
#Criate a diagonal Matrix with diag

arrFive  = np.diag(np.array([1,2,3,4]))

print(f"The diagonal matrix is: \n {arrFive}\n")


#Array with boolean values
arrSeix  = np.array([True, False, True, True])

#Array with strings
arrSeven  = np.array(["Python","R language", "Julia Language"])

print(f"The array string is:{arrSeven}")

#Criate a array with LINSPACE

'''
LINSPACE (Linearly Space Vector) criate a seuqnece of equals spaced numbers contais in a interval

'''

print(f"The array string is:\n{np.linspace(0,1)}\n")

'''
Log stapace do the same, but calculate the values in a log interval

'''

print(f"The array string is:\n{np.logspace(0,1,5)}\n")


