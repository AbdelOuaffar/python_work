def break_binary_single_digit(string):
    list_binary_digits = []
    for char in string:
        list_binary_digits.append(int(char))
    return list_binary_digits
def convert_binary_decimal(binary_list):
    decimal = 0
    rev_list = []
    rev_list += reversed(binary_list)
    for i in range(len(binary_list)):
        decimal += rev_list[i]*pow(2, i)

    return decimal
def main():

    binary_string = input("enter a binary number")
    binary_list = break_binary_single_digit(binary_string)
    result = convert_binary_decimal(binary_list)
    print(f"decimal number of {int(binary_string)} = {result}  ")
if __name__=="__main__":
    main()


#enter a binary number>? 1000
#decimal number of 1000 = 8


#enter a binary number>? 10001
#decimal number of 10001 = 17