def findInterectionUsingIn(list1, list2):
    intersection = []

    for i in list1:
        if i in list2:
            intersection.append(i)

    return intersection

def findIntersectionUsingNestedLoop(list1, list2):
    intersection = []
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                intersection.append(list1[i])

    return intersection


def addXToList(list, x):
    for i in range(0, len(list) - 1):
        list[i] = list[i] + x



list1=[1,0]
list2=[0,-1,-2,-4,-5,1]
common = findIntersectionUsingNestedLoop(list1, list2)
common= addXToList(common,1777)
print(common)

print(common)

# print(list1 and list2)
#print(common)
# def Comon_element
# for i in range(0,LEN(list1)-1):
#         for i in range(0,len(list2)-1):
#             if list1[i] == list2[i]:
#                 comon=list[i]
#
#