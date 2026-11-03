class student:
    

    def __init__(self,n,o,a):
        print("Hello Welcome BacK!")
        self.name=n
        self.occupation=o
        self.age=a

        

    def info(self):
        print(f"{self.name} is a {self.occupation} and is {self.age} years old")
a=student("Zoya","Singer",21)
print(a.info())