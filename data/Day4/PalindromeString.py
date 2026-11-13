user=input("Enter a String : ")
rev=user[::-1]
orignal=user
def isPlaindrome():
    if rev==orignal:
        print("String is palindrome ! ")
    else:
        print("String is not palindrome !")

isPlaindrome()
