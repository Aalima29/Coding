# Factorial (5)
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
        
#         fact=fact*i
#     print(fact)

# count digits

# def countdigit(n):
#     cnt=0
#     while (n>0):
#         cnt=cnt+1
#         n=n//10
#     print(cnt)
# countdigit(12345)

# Reverse a number
# def rev(n):
#     rev=0
#     while(n>0):
        
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     print(rev)
# rev(12345)



# Check Palin
# def isPalin(n):
#     rev=0
#     orignal=n
#     while(n>0):
        
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     if(rev==orignal):
#         return True
#     else:
#           return False
# print(isPalin(121))


# Print even 
# a=[10,20,39,45,60,67,80]
# for i in a:
#     if(i % 2 == 0):
#         print(i)


# count even
# a=[10,30,45,60,34,55,67]
# cnt=0
# for i in a:
#     if(i % 2 == 0):
#         cnt=cnt+1
# print(cnt)



# Find largest
# a=[10,20,40,80,45,32]
# largest=a[0]
# for i in a:
#     if(i>largest):
#         largest=i
# print(largest)

# Search for a number
# a=[10,20,30,40,60,50]
# target=99
# for i in a:
#     if(i==target):
#       print("Found!")
#       break
# else:
  
#       print("Not found")

# Calculate Sum
# a=[10,20,30,40,50]
# summ=0
# for i in a:
#     summ=summ+i
# print(summ)

# Reverse a list
# a=[10,20,30,40]
# rev=[]
# for i in range(4,-1,-1):
#     rev.append(i)
# print(rev)


# Find First Number Greater Then 50
# a=[10,20,52,30,40,50,55,60]
# largest=a[0]
# for i in a:
#     if(i>50):
#         print(i)
#         break

# print except negetive
# a=[10,-10,20,-20,30,-30,40,-40]
# for i in a:
#     if i>0:
#         print(i)
    

# print 2nd largest
# a=[10,20,30,50,60,80]
# largest=a[0]
# second_large=a[1]
# for i in a:
#     if(i>largest):
#         second_large=largest
#         largest=i
#     elif(i>second_large):
#         second_large=i
# print(second_large)

# remove dup
# a=[10,20,10,30,10,40,20,50,30,40,60,50]
# unique=[]
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)
    

# count freq
# a=[10,20,30,10,40,10,50,10,60]
# target=10
# cnt=0
# for i in a:
#     if i==target:
#         cnt=cnt+1
# print(cnt)


# find all num greater then avg
# a=[10,20,30,40,50,60,70]
# summ=0
# for i in a:
#     summ=summ+i
# avg=summ/len(a)
# for i in a:
#     if i>avg:
#         print(i)

# Seperate Even Odd
# a=[10,20,30,13,14,15,60,17]
# even=[]
# odd=[]
# for i in a:
#     if(i % 2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# move all zeroes to the end
# a=[0,10,0,20,0,30,0,40,0,0]
# cnt=0
# non_zero=[]
# for i in a:
#     if i!=0:
#         non_zero.append(i)
# for i in a:
#         if i==0:
             
#          cnt=cnt+1
#          non_zero.append(i)
# print(non_zero)


# Chec the list sorted
# a=[10,20,40,90]
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print("Not Sorted!")
#         break
# else:
#         print("Sorted")

# Check The Common Element
a=[1,2,4,6]
b=[1,2,7,8]

for i in a:
    
       if i in b:
          print(i)







