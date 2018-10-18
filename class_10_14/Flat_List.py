List = [  [1,[2]], "wish" ,[["Peace"],3]  ]
Flat = []

for el in List:
    if type(el)!= type(List):
        Flat.append(el)

    if type(el)== type(List):
       for el1 in el :
           if type(el1)!= type(List):
              Flat.append(el1)
           if type(el1)== type(List):
                for el2 in el1:
                   Flat.append(el2)


print(Flat)














