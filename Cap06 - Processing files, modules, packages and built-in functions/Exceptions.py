''''
Execeptions Try, Except, Finally

[PT]
O tratamento de erro serve para garantir que o usuário utilize o programa
da forma que ele foi desenvolvido. Portanto, vale sempre tentar pensar em
todos os erros possíveis

[EN]
Error handling serves to ensure that the user uses the program
the way it was developed. Therefore, it is always worth trying to think of
all possible mistakes

'''


# Create a new function
def numDiv(num1, num2):
    resultado = num1 / num2
    print(resultado)


try:

    numDiv(4, 2)
except:

    print("Something is wrong! See the insert numbers.")

finally:

    #Execute independent a error
    print("Finish")


############################################################

#Create a function
def askint():

    while True:
        try:
            val = int(input("Insert a number:"))
        except:
            print("It isnt a number!")
            continue
        else:
            print("Thaks for insert a number!")
            break

    print(f"The insert number is: {val}")
    print("Finish")



#Run function

askint()
























