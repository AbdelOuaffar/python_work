import sys


def abacus(st_int):
    i = 1
    v = 1

    while i <= len(st_int):

        var = st_int[len(st_int) - i]
        print(f"{v}z: {var}")
        i += 1
        v *= 10
try:
    str_int = input("Enter a string integer:\n ")

except IOError:
    print("str has letters ")# does not test the input
finally:
    print("end of coding")
abacus(str_int)
