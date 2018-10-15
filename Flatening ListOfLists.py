def  FlatenLists( mainList):
    Flat=[]
    for list in mainList:
        for item in list:
            Flat.append(item)
    print(Flat)
List = [[1,2,3],[4,5]]
FlatenLists(List)


