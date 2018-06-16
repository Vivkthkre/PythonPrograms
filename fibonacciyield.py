def fib(n):
    a, b=0, 1
    for i in range(n):
        yield a
        a, b=b, a+b
for f in fib(10):
    print(f)


#another:
def fib1():
    a, b=0, 1
    while True:
        yield a
        a, b=b, a+b
for f in fib1():
    if f>50:
        break
    print(f)
