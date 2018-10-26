def int_str(st):
    str_int_dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    i = 1
    v = 1
    integer = 0
    add = 0
    #while i <= len(st):
    for char in reversed(st):
        for key in str_int_dic:
            #if key == st[len(st)-i]:
            if key == char:
                integer +=  v*str_int_dic[key]
                add += str_int_dic[key]
                i += 1
                v *= 10
    return add, "sum of all the digits of the input ", integer, "is the integer type of the input", type(integer)
string = input("enter a string composed only with integers:")
result = int_str(string)
print(result)









