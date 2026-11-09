age1=int(input("Enter age 1 : "))
age2=int(input("Enter age 2 : "))
age3=int(input("Enter age 3 : "))
if age1<age2 and age1<age3:
    print("age 1 is smaller",age1)
elif(age2<age3 and age2<age1):
    print("age 2 is smaller",age2)
else:
    print("age 3 is smaller",age3)
