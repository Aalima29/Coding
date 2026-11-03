# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id

#     def showDetails(self):
#         print(f"The name of Employee is {self.name} with id {self.id}")

# class Programming(Employee):
#     def showLanguage(self):

#       print("The designation of this employee is Associate Trainee : ")

# e1=Employee("Aalima",101)
# e1.showDetails()
# e2=Programming("Zoya",102)
# e2.showDetails()
# e2.showLanguage()

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def make_Sound(self):
        print("Animals makes diff sounds")

class Dog(Animal):
    def __init__(self, name, breed  ):
        Animal.__init__(self,name, species="Dog")
        self.breed=breed

    def make_Sound(self):
        print("BArk!")

class Cat(Animal):
    def __init__(self, name, types):
        Animal.__init__(self,name,species="Cat")
        self.type=types

    def make_Sound(self):
        print("Meow!!")

E3=Cat("Dodo","Home")
Cat.make_Sound("Meow")



    