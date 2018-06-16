x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):   #for iterating through rows
    for j in range(len(x[0])):    # for  iterating column 
        result[i][j]=x[i][j]+y[i][j]

for r in result:
    print(r)
