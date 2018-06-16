fib_cache={}
def fibo(n):
    # if we have cache value then return
    if n in fib_cache:
        return fib_cache[n]
    #compute the nth term
    if n <= 1:
       return n
    else:
       value=fibo(n-1) + fibo(n-2)

    #cache the value and return it
    fib_cache[n]=value
    return value
        
n=int(input("Enter no. of terms:"))
for i in range(n):
    print(fibo(i))
