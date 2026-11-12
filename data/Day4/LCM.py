def lcm(x,y):
    if x>y:
        greater=y
    else:
        greater=x

    while True:
        if greater%x==0 and greater%y==0:
          result=greater
          break
        greater+=1
    return result
print("LCM of number is : ",lcm(12,24))
