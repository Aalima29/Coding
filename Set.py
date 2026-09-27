# s1={10,20,30,20,40}
# seen=set()
# for i in s1:
#     if i in seen:
#         print("Dup")
#     else:
#         print(seen.add(i))


# Count Unique Elements 
# s1={10,20,10,30,20,40,30,20,40}
# cnt=0
# for i in s1:
#     cnt=len(set(s1))
# print(cnt)

# check whether an elemnt exist
# s1={10,20,30,40}
# target=70
# for i in s1:
#     if target in s1:
#         print("Element exist!")
#         break
# else:

#     print("Element Not Exist")

# find common elemnts
# a1={10,20,30,40}
# b1={20,10,50,60}
# print(a1.intersection(b1))

# remove duplicates
# s1={10,20,30,40,10,20,30,40}
# unique=set()
# for i in s1:
#     if i not in unique:
#         unique.add(i)
# print(unique)
        
# s1=[10,20,10,30,20]
# seen=set()
# for i in s1:
#     if i  in seen:
      
#       print("Found",i)
#     else:
#       seen.add(i)

# Check if all elements are unique
# s1=[10,20,30,40]
# seen=set()
# for i in s1:
#     if i in seen:
#         print("Elements are not unique")
#     else:
#         seen.add(i)
# else:
#     print("all elements are unique")

# find elements present in a not in b
# s1={10,20,30,40}
# s2={10,20,50,60}
# print(s1-s2)

# find the first dup
# s1=[5,3,4,5,3,4]
# seen=set()
# for i in s1:
#     if i in seen:
#         print("found the first Duplicate",i)
#         break
#     else:
#         seen.add(i)

# Find the missing number
# s1={10,20,30,50}
# for i in range(10,51,10):
#     if i not in s1:
    
#         print("Missing number is ",i)

# find common element between two lists
# A = [10, 20, 30, 40, 50]
# B = [30, 40, 60, 70]
# s1=set(A)
# s2=set(B)
# print(s1.intersection(s2))

# check if two list having common element
# A = [1, 2, 3]
# B = [7, 8, 4]
# s1=set(A)
# s2=set(B)
# for i in s1:
#     if i in s2:
#         print("True",i)
#         break
# else:
#     print("False")

# Two Sum
a=[2,7,9,11]
target=9
seen=set()
for i in range(len(a)-1):
    curr_num=a[i]
    req_num=target-curr_num

    if req_num in seen:
        print("Found pair")
    else:
        seen.add(curr_num)




      
       


    