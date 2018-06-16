x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
#Using nested list comprehension
result=[[x[i][j]+y[i][j] for j in range
(len(x[0]))] for i in range(len(x))]
for r in result:
    print(r)
