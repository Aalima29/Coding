def isPalin(n):
    orignal=n
    rev=0
    

    while n>0:
     
     digit=n%10
     rev=rev*10+digit
     n=n//10

    if rev==orignal:
        return True
    else:
        return False
print(isPalin(121))