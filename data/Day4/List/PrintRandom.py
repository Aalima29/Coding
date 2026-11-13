num=[1,2,3,4]

for i in num:
    for j in num:
        for k in num:
            for l in num:
                if i!=j and i!=k and i!=l and j!=l and j!=k and k!=l:
                    print(i,j,k,sep=" ")