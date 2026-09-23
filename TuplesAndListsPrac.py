# tup=("Aalima","Zoya","Misbah","Jiya")
# temp=list(tup)
# temp.append("Mustafa")
# tup=tuple(temp)
# print(temp)

# KBC
# questions=["List is mutable ","Tuple is Immutable ","Fuctions are the block of code ","there are 2 types of func in Python "]
# answers=["Yes","Yes","yes","No"]
# amount=0
# for i,questions in enumerate(questions):
#     print(questions)
#     user_ans=input("Ans the question in Yes Or No only : ")
#     if(user_ans==answers[i]):
#        amount=amount+100
#        print("Amount Added",amount)
#     else:
#      print("Wrong")
#      break

    

# print(amount)

# String Format
# name="Zoya"
# city="Indore"
# print(f"My name is {name},I am from {city}")

# a=[10,20,30,40,50]
# for i in a:
#     print(i)


# Print only even numbers
# a=[2,4,6,8,7,5,3,10,12,14,59,89]
# for i in a:
#     if(i%2==0):
#         print (i)
#     else:
#         continue

# Count even
# a=[10,20,30,40,67,89,85,45]
# cnt=0
# for i in a:
    
#     if(i%2==0):
#         cnt=cnt+1
# print(cnt)

#Find largest Number
# a=[10,50,48,78,90,6]
# largest=a[0]
# for i in a:
#     if i>largest:
#         largest=i
# print(largest)


# Find the Smaller
# a=[40,89,67,1,56]
# small=a[0]
# for i in a:
#     if i<small:
#         small=i
# print(small)

# Search For a number 
# a=[10,20,30,40,50]
# target=80
# for i in a:
#     if i==target:
#         print("Found!")
# else:
#     print("Not found")


# a=[10,20,30,40,50]
# target=20
# for i ,a in enumerate(a):
#     if target==a:
        
#         print("Found! at index",i)
#     else:
#        continue
       

# a=[1,-2,2,-4,4,-5,5,-8,8]
# cnt=0
# for i in a:
#     if i>0:
#         cnt=cnt+1
# print(cnt)

# Calculate Sum
# a=[10,20,30,40,50]
# summ=0

# for i in a:
#     summ=summ+i
# print(summ)

# Reverse a list
# a=[10,20,30,40,50]
# rev=[]
# for i in range(4,-1,-1):
    
#     rev.append(a[i])
# print(rev)

# find first number greater then 50
# a=[10,20,30,45,56,52,78]
# greater=a[0]
# for i in a:
#     if i>50:
#         print(i)
#         break

# print number except negetive
# a=[10,-8,9,-7,6,-2,3,1]
# for i in a:
#     if(i>0):
#         print(i)


    
# Find second largest
# a=[10,20,30,50,60,40]
# largest=a[0]
# second_largest=a[1]
# for i in a:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif(i>second_largest):
#         second_largest=i
# print("Second largest number is : ",second_largest)


# remove duplicates
# a=[10,20,10,30,10,20,40,30,50,40]
# unique=[]
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# Count Frequency
# number=[10,20,10,30,10,40,10,50]
# target=10
# cnt=0
# for i in number:
#     if i==target:
#         cnt=cnt+1
# print(cnt)


# find all numbers greater then avg
# numbers=[10,20,30,40,50,60]
# summ=0
# for i in numbers:
#     summ=summ+i
# avg=summ/len(numbers)


# for i in numbers:
        
#  if i>avg:
#      print(i)
    
# Seperate Even and Odd
# number=[1,2,3,4,5,6,7,8,9]
# even=[]
# odd=[]
# for i in number:
#     if i%2==0:
#         even.append(i)
#     if(i%2!=0):
#         odd.append(i)
# print(even)
# print(odd)

# move all zeros to the end
# number=[0,10,20,0,30,40,0,90]
# rem=[]
# for i in number:
#     if i!=0:
#             rem.append(i)
# for i in number:
#     cnt=0

#     if i ==0:
#          cnt=cnt+1
#          rem.append(i)
     
    
        
# print(rem)


# Check if the list is sorted
# a=[10,20,40,60]

# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print("List is not  sorted")
#         break
# else:
#     print("List is  sorted")

# check the commen elements
a=[1,2,3,4]
b=[2,8,3,9]
for i in a:
    if i in b:
            print(i)
    


   


    



    


    




        
        
        




