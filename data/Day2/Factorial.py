def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        i=i+1
    print("Factorial of a number is",fact)
factorial(5)