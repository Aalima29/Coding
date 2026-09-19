# Use break and cont for searching what we have like searching for a num in array
# num=[10,20,30,40]
# for index,i in enumerate(num):
#     if(i==30):
#         print("Number is Found!",i,"at index : ",index)
#         break
#     print(i)

# Odd even
# for i in range(1,11):
#     if i%2!=0:
#         continue
#     print(i)

# Skip negative numbers
# num=[2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8,9,-9]
# for i in num:
#     if i<0:
#         continue
#     print(i)
#     i+1


# Find the first number greater than 50
# num=[10,20,30,40,50,55,60,70,80]
# for i in num:
#     if i>50:
#        print(i)
#        break


# give users correct password
# correct_password="python123"

# for i in range(3):
#     passw=(input("Enter a password "))
#     if(passw==correct_password):
#         print("Login succcessfull")
#         break
#     else:
#         print("Wrong password! logout")


# Skip multiples of 3

# Print numbers from 1 to 20, but skip numbers divisible by 3.
# for i in range(1,21):
#     if(i%3==0):
#         continue
#     print(i)
#     i+1

# Search for name
# name=["Zoya","Aalima","Misbah","Mummy","Daddy"]
# for i in name:
#     if(i=="Aalima"):
#         print("name found")
#         break


# Practice 10 — Mini challenge ⭐
while True:
    num=int (input("Enter a number"))
    
    if(num<0):
        continue
    elif(num==0):
        break
    else:
        print(num)

    
     
    


        
    