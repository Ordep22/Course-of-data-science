##Exercise number 1

from math import  sqrt

class Rocket():

    def __init__(self, x = 0, y =0):
        self.x = x
        self.y = y

    def MoveRocket(self,xIncrement = 0, yIncrement = 1):
        self.x += xIncrement
        self.y += yIncrement

    def PrintRocket(self):
        print(f"The cordenate of this rocket is ({self.x},{self.y})!")


#apollo11 = Rocket(10,10)
#apollo11.PrintRocket()

##Exercise number 2

class Person:

    def __init__(self):
        self.name = ""
        self.city  = ""
        self.phoneNumber = ""
        self.email = ""

    def Name(self,name):
        self.name = name
        print(f"The name this person is {self.name} ")


    def City(self,city):

        self.city = city
        print(f"{self.name} is from {self.city} ")

    def PhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
        print(f"{self.name}'s phone number is {self.phoneNumber} ")

    def Email(self, email):
        self.email = email
        print(f"{self.name}'s email is {self.email} \n\n")


personOne  = Person()
personOne.Name("Maria")
personOne.City("Juiz de Fora")
personOne.PhoneNumber("123456789")
personOne.Email("maria.python@empresa.com.br")


##Exercise number 3


class SmartPhone:

    def __init__(self):
        print("Criating a Smart Phone")

    def Size(self):

        print("The size os this smart phone is 128 Gb.")



    def Interface(self):

        print("The interface of this smart phone is Apple.")

    def PlayMusic(self):
        pass
    def StopMusic(self):
        pass



class MP3Player(SmartPhone):

    def __init__(self):
        SmartPhone.__init__(self)

    def PlayMusic(self):
        print("Taking music!")
    def StopMusic(self):
        print("Stoping Music!")


smartPhoneone = MP3Player()
smartPhoneone.Interface()
smartPhoneone.Size()
smartPhoneone.PlayMusic()
smartPhoneone.StopMusic()










