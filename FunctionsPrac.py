# def greet(name):
#     a=name
#     print("Hello ",a)

# name=input("Enter your name: ")
# greet(name)
    

# Add two Numbers
# def Addnum(a,b):
#     sum=a+b
#     print(sum)

# a=int(input("Enter first number "))
# b=int(input("Enter 2nd number "))
# Addnum(a,b)


# Square of a number
# def square(n):
#     num=n*n
#     print(num)

# a=int(input("Enter a number to calculate Square : "))
# square(a)


# Even_Odd
# def checkEO(n):
#     if(n%2==0):
#         print("Number is even!")
#     else:
#         print("Number is odd!")

# a=int(input("Enter a number to check even odd : "))
# checkEO(a)


# find the greater number
# def findGreat(a,b):
#     if(a>b):
#         print("a is greater!")
#     else:
#         print("b is greater!")

# a=int(input("Enter first number "))
# b=int(input("Enter Second number "))
# findGreat(a,b)

# Largest of three
# def largestOfThree(a,b,c):
#     if(a>b and a>c):
#         print("a is greater! ")
#     elif(b>a and b>c):
#         print("b is greater!")
#     else:
#         print("c is greater!")

# a=int(input("Enter value of a"))
# b=int(input("Enter value of b"))
# c=int(input("Enter value of c"))
# largestOfThree(a,b,c)

# print numbers
# n=0
# def printNum(n):
#     for i in range(1,n):
#         print(i)

# num=int(input("Enter a number "))
# printNum(num)


# Sum from 1 to n

# def sumtoN(n):
#     for i in range(1,n):
#         sum=i+1
#         print(sum)
# a=int(input("Enter a number "))
# sumtoN(a)


# Count even

# a=[10,20,30,35,5,8]
# def counteven(num):
#     cnt=0
    
#     for i in num:
        
#         if i%2==0:
#             cnt=cnt+1
#     return cnt
# print(counteven(a))


# find first number greater then 50
# a=[10,30,50,55,60,80]
# def findGreat(num):
#     for i in num:
#         if(i>50):
#             print(i)
#             break

# print(findGreat(a))



# Find number
# number=[10,20,30,40,50]
# def findNum(search,number):
#     for i in number:
#         if(i==number):
#             print("Number Found")
#             break
# findNum(30,number)
 

# 14. Calculator
# def Calculator(a,b,operator):
#     if(operator== "+"):
#         sum=a+b
#         print(sum)
#     elif(operator=="-"):
#         sub=a-b
#         print(sub)
#     elif(operator=="*"):
#         mul=a*b
#         print(mul)
#     else:
#         div=a/b
#         print(div)

# Calculator(60,20,"/")


# Factorial****
# def facorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# facorial(5)

# count digits****


# def countdigits(n):
#     cnt=0
#     while(n>0):

        
#         cnt=cnt+1
#         n=n//10
#     print(cnt)
# countdigits(12345)

# Reverse a number****

# def reverse(n):
#     rev=0
#     while(n>0):
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     print(rev)

# reverse(12345)

# check Palindrome
# def isPalindrome(n):
#     orignal=n
#     rev=0
#     while(n>0):
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     if(orignal==rev):
#         return True
#     else:
#         return False
# print(isPalindrome(123))


# Prime number
def isPrime(n):
    while(n>0):
        if(n%2!=0):
            return True
        else:
            return False
print(isPrime(10))