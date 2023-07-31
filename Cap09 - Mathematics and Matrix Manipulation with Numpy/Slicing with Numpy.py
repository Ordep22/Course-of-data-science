import numpy as np

#Criating a diagonal mat
arrayOne  = np.diag(np.arange(3))

print(f"The diagonal math is:\n{arrayOne}")

#So, we can find the espcifc elements in the array. For that we can use the slicing method

#To find an elements in the mat
elOneone  =  arrayOne[1,1]

print(f"The elemnt in the line one and columun one is: {elOneone}")

#To find a full line in the mat

lineOne = arrayOne[1]

print(f"The line one in the mat is: {lineOne}")

#To find a full column in the mat

columnZero = arrayOne[:,0]

print(f"To find a column in the mat: {columnZero}")

#Criating a range

arrayTow = np.arange(10)

print(f"The array tow is: {arrayTow}")

#Slincing in the array Tow

print(f"The slicing method in the arrayTow is: {arrayTow[2:9:3]}")

#Comparing the elements in the array

arrayThree = np.array([1,2,3,4,5])

arrayFour = np.array([5,4,3,2,1])

print(f"The chek elements was: {arrayThree == arrayFour}")

#Compare if the arrays are equals. The method np.array_equal returns true or false depending if the elements in the array are equals.


compration = np.array_equal(arrayThree,arrayFour)

print(f"The comparatio betwem arrayThree and arrayFour is: {compration}")


#Sum a constat value in an array

arrayFive  = np.array([11,12,13,14,15,16])

print(f"The array Five is: {arrayFive}")

print(f"The sum in the array five resul in:{arrayFive + 3.14}")

#If we can arround the velues in the array, we can use the method arroud()

print(f"The aproximed values on array five is: {np.around(arrayFive)}")

















