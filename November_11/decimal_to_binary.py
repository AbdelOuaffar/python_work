def remainders(decimal):
    list_remainders = []
    quotient = 2
    while quotient != 1:
        quotient = decimal//2
        rem = decimal % 2
        list_remainders.append(rem)
        decimal = quotient
    list_remainders.append(quotient)
    list_remainders.reverse()
    return list_remainders

def binary_string(list):
    binary = ""
    for element in list:
        binary += str(element)
    return binary
def main():
    decimal = int(input("enter a decimal number"))
    list_rem = remainders(decimal)
    result = binary_string(list_rem)
    print(f"binary number equivalent to {decimal} ={result}")
if __name__=="__main__":
    main()


#enter a decimal number>? 20
#binary number equivalent to 20 =10100

#enter a decimal number>? 8
#binary number equivalent to 8 =1000