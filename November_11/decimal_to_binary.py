def remainders(decimal):
    quotient = decimal//2
    rem = decimal % 2
    list_remainders.append(rem)
    decimal = quotient
    if quotient == 1 and (rem == 0 or 1):
        list_remainders.append(quotient)
        return list_remainders.reverse()
    return remainders(decimal)
def binary_string(list):
    binary = ""
    for element in list:
        binary += str(element)
    return binary
def main():
    global list_remainders
    list_remainders = []
    decimal = int(input("enter a decimal number"))
    remainders(decimal)
    result = binary_string(list_remainders)
    print(f"binary number equivalent to {decimal} ={result}")
if __name__=="__main__":
    main()
#enter a decimal number>? 16
#binary number equivalent to 16 =10000

#enter a decimal number>? 5
#binary number equivalent to 5 =101


#enter a decimal number>? 12
#binary number equivalent to 12 =1100



