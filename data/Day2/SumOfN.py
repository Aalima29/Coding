def sumOfNum(n):
    
 if n<0:
    print("Not a natural number")
 else:
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        i=i+1
    print("Sum of Natural number is",sum)
sumOfNum(-10)