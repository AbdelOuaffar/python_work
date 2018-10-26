import sys

import sys
def str_to_int(str):
    multiplier = 1
    for char in reversed(str):
        print(f"{multiplier} - {char}")
        multiplier *= 10


def __main__():
    if len(sys.argv) < 2:
        print("Please pass an argument to convert to an integer.")
        return

    str_to_int(sys.argv[1])


__main__()
