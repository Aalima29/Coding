# print numbers from 1 to N
# def printNum(n):
#     if n == 0:
#         return
#     printNum(n-1)
#     print(n)
    
# printNum(5)


# print even
# def Even(n):
#     if n<=0:
#         return 
#     if n% 2 != 0:
#         return
#     Even(n-2)
#     print(n)
    
# Even(10)

# FInd the sum from 1 to n
# def findSum(n):
#     if n == 0:
#         return 0
    
#     return n+findSum(n-1)
# print(findSum(5))

# count digits
# def Summ(n):
#     if n==0:
#         return 0
#     return n%10+Summ(n//10)
# print(Summ(564))

def reverse(n,rev=0):
    if n==0:
        return rev
    digit=n%10
    rev=rev*10+digit
    n=n//10
    return reverse(n,rev)
print(reverse(12345))
