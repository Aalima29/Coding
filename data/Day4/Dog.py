head=int(input("Enter number of heads : "))
legs=int(input("Enter number of legs"))

dogs=(legs-2*head)//2
chicken=head-dogs
if dogs>=0 and chicken>=0 and (legs-2*head)%2==0:
    print("number of dogs",dogs)
    print("number of chicken",chicken)
else:
    print("Invalid")




