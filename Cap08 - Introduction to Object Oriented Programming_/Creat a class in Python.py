

"""
[EN]


[PT]


"""

#Criate a class

class Boock():

    #This method will initialize each object of this class
    # The name of this method is __Init__
    # Self is a reference to each attribute of the class itself (not a parent class)
    def  __init__(self):
        #Attributes are proprietors
        self.title = "Clean code"
        self.isbn = 12345678
        #print("Contructor called to criate a object in this class.")

    def show(self):
        print(f"Was criate a book {self.title} wih ISBN {self.isbn}")

##Criating a intance of the boock classes
boockOne  = Boock()

##Show what is the type of boockOne
print(f"The type of boockOne is:{type(boockOne)}")
'''output  -> The type of boockOne is:<class '__main__.Boock'>'''

#Show the attributes to this class
print(f"The title of boock one is: {boockOne.title}")

class BookTow():

    def __init__(self,title,isbn):

        self.title  =  title
        self.isbn = isbn
        print("Contructor called to criate a object in this class.")

    def show(self, title, isbn):
        print(f"The title of the insert book is {self.title} and it´s ISBN is {self.isbn}")


boockTow = BookTow("The Hobbit", 987456133)

boockTow.show("The Hobbit", 987456133)










