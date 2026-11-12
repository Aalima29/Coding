n=int(input("Enter any number : "))
summ=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    summ=summ+(i/fact)
print("Sum of n number is : ",summ)
  