num=int(input("Enter 3 digit number :"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp//=10
if sum==num:
    print("The number is armstrong number")
else:
    print("The number is not an armstrong number")
