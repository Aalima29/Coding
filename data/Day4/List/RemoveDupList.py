a=[1,2,3,4,2,4,5,3]
seen=[]
for i in a:
    if i not in seen:
        seen.append(i)
    
print(seen)

