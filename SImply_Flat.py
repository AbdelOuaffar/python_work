def peeler(n_dimension_list):
    for element in n_dimension_list:
        if type(element) == type(n_dimension_list):
            peeler(element)
        else:
            Final_List.append(element)


Final_List = []
Init_List = [[[[23, "Reg"]]], "think", [[[789, [[[[[[[["QQQQ"]]]]]]]]]]]]
peeler(Init_List)
print(Final_List)
