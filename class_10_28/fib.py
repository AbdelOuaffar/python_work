def fib(n):
    a = 0
    b = 1
    x = 0
    for i in range(n):
        a = b
        b = x
        x = a + b
    return x
n = int(input("enter a number: "))
if n >= 0:
 result = fib(n)
 print(f"fib({n})= {result} ")
else:
    m = -n
    result = -fib(m)
    print(f"fib({n})= {result} ")
