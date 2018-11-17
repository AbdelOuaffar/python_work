def grand_c_d(a, b):
    r = 1
    x = a
    y = b
    while r != 0:
        r = a % b
        if r != 0:
            a = b
            b = r
    print(f"GCD({x},{y})={b}")

def main():
    a = int(input("enter first integer:"))
    b = int(input("enter second integer"))
    if a == 0 and b != 0:
        print(f"GCD({a},{b})={b}")
    elif a != 0 and b == 0:
        print(f"GCD({a},{b})={a}")
    elif a == 0 and b == 0:
        print("there is none for (0,0)")
    elif a >= b:
        grand_c_d(a, b)
    else:
        grand_c_d(b, a)
if __name__=="__main__":
    main()


#enter first integer:>? 123
#enter second integer>? 12
#GCD(123,12)=3

#enter first integer:>? 120
#enter second integer>? 12
#GCD(120,12)=12

#enter first integer:>? 0
#enter second integer>? 34
#GCD(0,34)=34

