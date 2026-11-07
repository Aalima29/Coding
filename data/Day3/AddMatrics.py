A=[[1 , 5 , 6],
   [2 , 4 , 8],
   [3 , 9 , 7]]
B=[[4 , 7 , 1],
   [8 , 2 , 9],
   [10 ,4 , 7]]

result=[[0 , 0 , 0],
        [0 , 0 , 0],
        [0 , 0 , 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
for r in result:
     print(result)
