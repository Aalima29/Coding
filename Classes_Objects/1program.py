class student:
    name="aalima"
    age=21
    occupation="Software Eng"
    def info(self):
        print(f"{self.name},is a {self.occupation}")
a=student()
a.name="Misbah"
a.occupation="Artist"
b=student()
b.name="Zafar"
b.occupation="Principal"
print(a.info())