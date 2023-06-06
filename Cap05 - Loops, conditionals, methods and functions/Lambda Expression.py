"""
Function Lambda
It's a spaecial function in Python and it's most implemented in
Data Science
It's an anonymous function as it's used at the time of execution

"""
#For our best understanding, we will compare the normal function with a
#lambda function

#It's a normal function
def sum1(num1,num2):
    resultado  = num1 + num2
    return  print(resultado)

sum1(1,2)

#But, it's necessary to simplif more the function. So we can use Lambda Expressions.
sum2  = lambda num: num + num * 2

print(f"The result of lambda expression is:{sum2(1)}")
