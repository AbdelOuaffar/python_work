def  Flat_Lst(list):
    for element in list:
        while type(element)== type (list):
            for elm in element:
                Flat.append(elm)
        if type(element) != type(list):
            Flat.append(element)
    print(Flat)
List = [[1,2],"wish",["Peace",3]]
Flat = []
Flat_lst(List)











