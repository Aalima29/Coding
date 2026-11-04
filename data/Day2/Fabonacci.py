def fabonacci(n):
    a=0
    b=1
    if n==1:
        print(b)
    else:
     print(a)
     print(b)
     for i in range(1,n+1):
       
        c=a+b
        a=b
        b=c
        
        print("The fabonacci series are",c)
fabonacci(8)
 