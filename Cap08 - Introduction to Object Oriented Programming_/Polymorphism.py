"""
[EN]
 The word "polymorphism" means "many forms", and in programming it refers
 to methods/functions/operators with the same name that can be executed
 on many objects or classes.

[PT]
A palavra "polimorfismo" significa "muitas formas", e na programação refere-se
a métodos/funções/operadores com o mesmo nome que podem ser executados
em muitos objetos ou classes.

"""

class Vehicle:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def SpeedUp(self):
        pass

    def Brake(self):
        pass

class Car(Vehicle):

    def SpeedUp(self):
        print("The car is accelerating!!!")

    def Brake(self):
        print("The car is braking")

class Motorcycle(Vehicle):

    def SpeedUp(self):
        print("The mortocycle is accelerating!!!")

    def Brake(self):
        print("The mortocycle is braking")

    def  Cram(self):
        print("Runm")


#Creating a list of instace classes objects
listVehicles  = [Car("Prosche","911 Turbo"), Motorcycle("Honda","CB 1000R Black Edition")]

for iten in listVehicles:
    #Method Brake
    iten.Brake()

    #Method Speed Up
    iten.SpeedUp()

    if isinstance(iten,Motorcycle):
        iten.Cram()

    print(10*"----")
