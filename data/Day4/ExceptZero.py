summ=0
count=0
num=int(input("Enter a number "))
while (num!=0):
    print("You Entered ",num)
    
    summ=summ+num
    count=count+1
    num=int(input("Enter another number : "))
if count>0:
    avg=summ/count
    print("Sum of number is ",summ)
    print("Avg of number is ",avg)
else:
    print("No num entered ")

