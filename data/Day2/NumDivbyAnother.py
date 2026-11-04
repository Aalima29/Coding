lower=int(input("Enter lower range"))
upper=int(input("Enter upper range"))
num=int(input("Enter number to be divided"))

for i in range(lower,upper+1):
    if i%num==0:
        print("The number divided by",num , "are ",i)