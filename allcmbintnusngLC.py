n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
n3=int(input("Enter number3:"))
n=[n1,n2,n3]
#using list comprehension
print("Using list comprehension")
l=[print(i,j,k) for i in n for j in n for k in n]
