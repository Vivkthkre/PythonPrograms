# Python program to display the Fibonacci sequence up to n-th term using recursive functions

from functools import lru_cache
@lru_cache(maxsize=100)
 # the above statements are used because for greater value of n(n>25) the program begins to slow down
 # so cache is used to increase the speed, it is also called memoization.
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
        
n=int(input("Enter no. of terms:"))
for i in range(n):
    print(fibo(i))
    
