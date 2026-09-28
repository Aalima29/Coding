# # info={
# #     'name':'Zoya',
# #     'age':21,
# #     'Qualification':'B.Tech',
# #     'Hobbies':'Singing'
# # }
# # for keys in info.keys():
# #     print(f"The Value Corresponding to key {keys} is {info[keys]}")

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
# a = [2, 3, 2, 5, 3, 2]
# freq={}

# for i in a:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# Char freq
# s="banana"
# freq={}
# for ch in s:
#     if ch not in freq:
#         freq[ch]=1
#     else:
#         freq[ch]+=1
# print(freq)


# find the first element that appears twice
# a=[1,2,1,3,2,4]
# seen={}
# for i in a:
#     if i in seen:
#         print(i)
#         break
#     else:
#         seen[i]=1
# print(seen)

# Two sum with dict
# a=[2,7,11,17]
# target=9
# num={}
# for i in a:
#     req_num=target-i
#     if req_num in num:
#         print("pair Found",req_num,i)
#         break
#     else:
#         num[i]=True


# Q1. Count Frequency
# a = [1, 2, 2, 3, 1, 1, 4]
# freq={}

# for i in a:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)


# Q2. Check Element
# a = [10, 20, 30, 40, 50]
# target=30
# for i in a:
#     if i==target:
#         print("Number exist")
#         break
# else:
#     print("Not exist")

# Finding Duplicate in dictonary
# a = [10, 20, 30, 20, 40, 10, 50, 30]
# seen={}
# for i in a:
#     if i in seen:
#         print("Duplicate exist",i)
#     else:
#         seen[i]=True
# print(seen)

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
# a = [1, 3, 2, 3, 4, 3, 2]
# seen={}
# cnt=0
# max_num=0

# for i in a:
#     if i not in seen:
#         seen[i]=1
#     else:
#         seen[i]+=1


# for i in seen:
#     if seen[i]>cnt:
#         cnt=seen[i]
#         max_num=i
# print("Max freq of num ",max_num,"is",cnt)


# Find the first non repeating char
# s = "aabbcddee"
# seen={}
# for ch in s:
#     if ch not in seen:
#         seen[ch]=1
#     else:
#         seen[ch]+=1

# print(seen)
# for ch in seen:
#     if seen[ch] ==1:
#         print(ch)
#         break

# Find Common Element using a dictionary
# A = [10, 20, 30, 40]
# B = [30, 40, 50, 60]
# seen={}
# for i in A:
#     seen[i]=True
# for i in B:
#         if i in seen:
#          print(i)

# find missing number
# a = [1, 2, 3, 5, 6]
# seen={}
# for i in a:
#     seen[i]=True
# for i in range(1,7,1):
#     if i not in seen:
#         print("Missing number is",i)

# check anagrams
s1 = "listen"
s2 = "silend"
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
        print ("false")
print("true")









