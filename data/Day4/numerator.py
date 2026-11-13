num=int(input("Enter Numerator "))
denom=int(input("Enter Denominator "))
hcf=1
for i in range(1,min(num,denom)+1):
    if num%i==0 and denom%i==0:
        hcf=i
new_num=num//hcf
new_denom=denom//hcf
print("The result is ",new_num,"/",new_denom)