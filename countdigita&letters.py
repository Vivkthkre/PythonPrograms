st=input("Enter string:")
num=0
s=0
for i in st:
    if i.isdigit():
        num+=1
    else:
        s+=1
print('No. of digits=',num)
print('No. of letters=',s)
