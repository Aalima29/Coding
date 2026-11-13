ls=[10,20,90,40,50]
for i in range(len(ls)-1):
    if ls[i]<ls[i+1]:
        print("List is in ascending order")
        
    else:
        print("not in ascending oreder")
        break