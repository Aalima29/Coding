ls=[10,20,30,40]
print("This is your list : ",ls)
old=int(input("Enter the number you want to replace : "))
new_num=int(input("Enter the number you want to add on that place"))
if old in ls:
    for i in range(len(ls)):
        if ls[i]==old:
            ls[i]=new_num
    print("The updated list is : ",ls)
else:
    print("Number not found")

    
