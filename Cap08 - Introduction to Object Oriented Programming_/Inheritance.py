"""
[EN]
Inheritance allows us to define a class that inherits all the methods and
proprieties from another class. Parent class is the class being inherited from,
also called base class. Child class is the class that inheits from another class, also
called derived class.

[PT]
A herança nos permite definir uma classe que herda todos os métodos e
propriedades de outra classe. A classe pai é a classe da qual está sendo
herdada, também chamada de classe base. Classe filha é a classe que
herda de outra classe, também chamada de classe derivada.

"""
from pygame import  mixer

class Animal:
    def __init__(self):
        print("Criating an animal!")
    def imprimir(self):
        print("This is a animal")

    def eat(self):
        print("Time to eat")
    def MakeNoize(self):
        pass


class Dog(Animal):
    def __init__(self):

        Animal.__init__(self)

        print("Object Dog  was criate!")

    def MakeNoize(self):

        mixer.init()
        mixer.music.load("/Users/PedroVitorPereira/Documents/GitHub/Python_Projects/Course-of-data-science/Cap08 - Introduction to Object Oriented Programming_/SmallDog.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()
        #mixer.music.stop()

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)

        print("Object Cat  was criate!")

    def MakeNoize(self):
        mixer.init()
        mixer.music.load("/Users/PedroVitorPereira/Documents/GitHub/Python_Projects/Course-of-data-science/Cap08 - Introduction to Object Oriented Programming_/SmallCat.mp3")
        mixer.music.set_volume(50)
        mixer.music.play()
        mixer.music.unpause()


meleca  = Cat()
meleca.MakeNoize()
meleca.eat()

