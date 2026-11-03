class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")

@property
def value(self):
    return 10*self._value

# if i want to update the value then i use setters
@value.setter
def _value(self,new_value):
    self._value=new_value/10



obj=Myclass(10)
obj._value=67
print(obj._value)
obj.show()
