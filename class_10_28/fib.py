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
def main():

        if len(sys.argv) == 3:
            try:
             if sys.argv[1] == "fib":
                 n = int(sys.argv[2])
                 if n >= 0:
                      result = fib(n)
                 elif n < 0:
                      result = - fib(-n)
                 print(result)
            except ValueError:
                 print("check if your input is numeric")
            finally:
                   print("EOScript")
main()







