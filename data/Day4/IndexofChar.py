user=input("Enter a String : ")
char=input("Enter a character : ")
found=False

for i in range(len(user)):
    if user[i]==char:
        print("The index of character",char,"is : " ,i)
        found=True
if not found:
    print("Character not found")