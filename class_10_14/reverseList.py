def reverseList(list):
    end = len(list) - 1
    newList = []
    while end >= 0:
        newList.append(list[end])
        end = end - 1

    return newList

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def reverseListOptimized(list):
    start = 0
    end = len(list) - 1
    while start < end:
        swap(list, start, end)
        start = start + 1
        end = end - 1




list1 = [1,2,3,4]
print(list1)

list1Reversed = reverseListOptimized(list1)

print(list1)

