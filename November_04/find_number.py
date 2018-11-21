import bisect


def linear_search(numbers, number):
    for element in numbers:
        if element == number:
            print("your number is in the list")
            return
    print("done")


def binary_search(numbers, number):
    return bisect.bisect(numbers, number)


number = int(input('enter a num: '))
numbers = list(range(100000))

linear_search(numbers, number)

print("done linear search")

binary_search(numbers, number)

print("done binary search")
