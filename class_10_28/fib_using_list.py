def fib_list_2index(n):
    fib_base = [0, 1]
    for i in range(n-1):
        fib_base.append(fib_base[1] + fib_base[0])
        del(fib_base[0])
    return fib_base[1]
n = int(input("enter a number: "))
result = fib_list_2index(n)
print(f"fib({n}) = {result}")

#Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
#runfile('C:/Users/PC/python_work/class_10_28/fib_using_list.py', wdir='C:/Users/PC/python_work/class_10_28')
#enter a number: >? 5
#fib(5) = 5
#enter a number: >? 30
#fib(30) = 832040
#enter a number: >? 0
#fib(0) = 1