user=input("enter any string : ")
rem=input("enter a character that you want to remove : ")

if rem in user:
        user=user.replace(rem," ")
        print("After removing the string will be :",user)
else:
    print("you enter wrong character ")



