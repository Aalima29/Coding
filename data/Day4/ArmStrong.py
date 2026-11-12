user=int(input("Enter 3 number : "))
temp=user
sum=0
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp//=10

if user==sum:
        print("Armstrong number")
else:
        print("Not an Armstrong number")
