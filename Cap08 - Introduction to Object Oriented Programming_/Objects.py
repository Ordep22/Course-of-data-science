#Criate a list in python

lisOne  =  ["Data","Science","Academy", "Nota", 10, 10]

#The list LiostOne is a object, an instance of the class list in Python

print(f"The of listOne is: {type(lisOne)}")


#Everithing we criate with [] the Python language undertand that is a list
#So we can afirm all in Ptyhon is an object

print(f"The of listOne is: {type(lisOne)}")

class Employee():

    def __int__(self, name, wage, office):

        self.name =  name
        self.wage = wage
        self.office = office

    def listEmployee(self):
        print(f"Employee {self.name}, {self.wage}, {self.office}")

EmployeeOne  = Employee("Mary",2000,"Engineer")

EmployeeOne.listEmployee()
