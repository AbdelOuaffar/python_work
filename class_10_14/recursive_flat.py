def flat(list):
    if type(list[0]) != type([]):
        return  list

    final_list = []
    for sub_list in list:
        for element in sub_list:
            final_list.append(element)

    return final_list


def flatN(list):
    flattened_list = flat(list)
    while type(flattened_list[0]) == type([]):
        flattened_list = flat(flattened_list)

    return flattened_list

def flatN_recursive(list):
        if type(list[0]) != type([]):
            return list

        final_list = []
        for sub_list in list:
           flattend = flat(sub_list)
           final_list  += flatN_recursive(flattend)
        return  final_list

test_list = [[[[1, 2]], [[3, 4]]]]
result = flatN_recursive(test_list)
print(result)
# [1,2,3,4]
