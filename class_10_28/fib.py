import sys
def fib(n):
    a = 0
    b = 1
    x = 0
    for i in range(n):
        a = b
        b = x
        x = a + b
    return x
def __main__():

        if len(sys.argv) < 2:
             print("enter an argument")
             return
        try:
          n = int(sys.argv[1])
          if n >= 0:
                result = fib(n)
          elif n < 0:
                result = - fib(-n)
          print(result)
        except ValueError:

                print("check if your input is numeric")
        finally:
            print("EOScript")
__main__()









#n = int(input("enter a number: "))
#if n >= 0:
 #result = fib(n)
# print(f"fib({n})= {result} ")
#else:
   # m = -n
    #result = -fib(m)
   # print(f"fib({n})= {result} ")
