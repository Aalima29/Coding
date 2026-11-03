# def sumtoN(n):
#     s=0
#     for i in range(1,n):
       
#         s=s+i
#     print("Sum = ",s)
# a=int(input("Enter a number : "))
# sumtoN(a)


# a=[10,20,55,50,45]

# def FirstGreat(n):
#     for i in n:
#         if i>50:


#          print("First Greater Num is :",i)
#          break

#     else:
#            print("No one is greater")
# print(FirstGreat(a))


# a=[10,20,30,40]
# target=50
# def FindNum(n):
#     for i in n:
#         if i==target:
#             print("Number Found",i)
#             break
#     else:
#         print("Not Found!")
# FindNum(a)


# a=[10,20,30,40]
# find=0
# def findNum(n):
#     for i in n:
#         find=i+10
#     print("Next Number is :",find)
# findNum(a)



# def findFact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
        
#     print(fact)

# findFact(5)
    

# def countDigit(n):
#     count=0
#     while(n>0):
      
#       count=count+1
#       n=n//10
#     print(count)
# countDigit(12345)

# def reverseNum(n):
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     return rev
# print(reverseNum(12345))

# Check Palindrome
# def isPalindrome(n):
#     orignal=n
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=rev*10+digit
#         n=n//10
#     if(rev==orignal):
#         return True
#     else:
#         return False
# print(isPalindrome(128))



# Count Unique
# s1=[10,20,30,40,10,20,30,40]
# unique=[]
# cnt=0
# for i in s1:
#     if i not in unique:
#         unique.append(i)
# print("Unique Elements",unique)
# print("Count",len(unique))


# # check whether an elemnt exist
# s1={10,20,30,40}
# target=20
# for i in s1:
#     if i==target:
#         print("Element Exist",i)
#         break
# else:
#     print("Element Not Exist!")
    
# Remove dup
# s1={10,20,30,40,10,20,30,40}
# seen=set()
# for i in s1:
#     if i not in seen:
#         seen.add(i)
# print(seen)


# Check if all elements are unique
# s1=[10,20,30,40]
# seen=set()
# for i in s1:
#     if i in seen:
#         print("Elements are nor unique")
#         break
#     else:
#         seen.add(i)
        
# else:
#     print("Elements are unique")

# # find elements present in a not in b
# s1={10,20,30,40}
# s2={10,20,60,70}
# print(s1.difference(s2))


# find the first duplicate
# s1=[5,3,4,5,3,4]
# seen=set()
# for i in s1:
#     if i in seen:
#         print("Duplicate Found",i)
#         break
#     else:
#         seen.add(i)
# else:
#     print("No Duplicate Found!")

# find the missing number
# s1={10,20,30,50}
# for i in range(10,51,10):
#     if i not in s1:
#         print("Missing number is",i)

# a=[2,7,9,11]
# target=11
# seen=set()
# for i in range(len(a)-1):
#     curr_num=a[i]
#     req_num=target-curr_num
#     if req_num in seen:
#      print("Pair Found!",req_num,curr_num)
#     else:
#      seen.add(curr_num)


# a1={
#     68:'Aalima',
#     169:'Abhijeet',
#     172:'Aditya',
#     189:'Avni',
#     190:'Anuj'
# }
# a2={
#     154:'Shatakshi',
#     158:'Nawadha',
#     159:'Surbhi',
#     180:'Rhythm'
# }
# a1.update(a2)
# print(a1)

# freq Count
# a="a1b2c3d4"
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]=freq[i]+1
#     else:
#         freq[i]=1
# for i in freq:
#     print(i,freq[i])


# s="a2b3c4d5"
# result=""
# i=0
# while(i<len(s)):
#     char=s[i]
#     num=int(s[i+1])
#     result+=char*num
#     i+=2
# print(result)

# Char freq
# a="banana"
# freq={}
# i=0
# for ch in a:
#     if ch not in freq:
#         freq[ch]=1
#     else:
#         freq[ch]=freq[ch]+1
# for ch in freq:
#     print(ch,freq[ch]) 

# find the first element that appears twice
# a=[1,2,1,3,2,4]
# seen={}
# for i in a:
#     if i in seen:
#         print("The first appeared number is : ",i)
#         break
#     else:
#         seen[i]=1

# Check Element
# a = [10, 20, 30, 40, 50]
# target=30
# for i in a:
#    if i == target:
#         print("Number Exist!")
#         break
# else:
#         print("Not Exist")

# Finding Duplicate in dictonary
# a = [10, 20, 30, 20, 40, 10, 50, 30]
# seen={}
# for i in a:
#     if i in seen:
#         print("Duplicate",i)
#     else:
#         seen[i]=True


# Count characters
# s="programming"

# char={}
# cnt=0
# for ch in s:
#     if ch in char:
#         cnt+=1
#     else:
#         char[ch]=cnt
# print(char)

# Find the elemnt with the highest freq
# a=[10,20,30,10,20,40,10,40,30,10]
# cnt=0
# max_num=0
# freq={}
# for i in a:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]>cnt:
#         cnt=freq[i]
#         max_num=i
#         print("The Element with the highest freq is",max_num,cnt)

# Find the first non repeating char
# s = "aabbcddee"
# seen={}

# for i in s:
#     if i in seen:
#         continue
# else:
#     print(i)


# find missing number
# a = [1, 2, 3, 5, 6]
# missing={}
# for i in a:
#     missing[i]=True
# for i in range(1,7,1):
    
#     if i not in missing:
#         print("Missing number is",i)


# Check Anagram
s1="Silent"
s2="lienSt"
seen={}
if len(s1)!=len(s2):
    print("False")

for ch in s1:
    if ch not in seen:
        seen[ch]=1
    else:
        seen[ch]+=1
for ch in s2:
    if ch not in seen:
        print("False")
        break
    else:
        seen[ch]-=1
for ch in seen:
    if seen[ch]!=0:
        print("False")


print("True") 






    










    
