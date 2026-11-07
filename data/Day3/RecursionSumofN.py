def sumOfNum(n):
    if n<=1:
        return n
    else:
        return n+sumOfNum(n-1)
print("Sum of N Natural Number is ",sumOfNum(10))