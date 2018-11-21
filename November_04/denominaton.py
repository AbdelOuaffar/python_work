import sys

def  break_money_to_denom(money_sum):
    denomination = {"hundreds": 100, "twenties": 20, "tens": 10, "fives": 5, "twos": 2, "ones": 1, "quarters": .25, "dimes" : .10, "nickles": .05, "pennies": .01}


    money = float(money_sum)
    for key in denomination:
            if money >= denomination[key]:
                number = money//denomination[key]
                reminder = money % denomination[key]
                print(key, number)
                money = reminder
def main():

         if len(sys.argv) <= 2:

            string = sys.argv[1]
            break_money_to_denom(float(string))

         else:
            print("ytytu")





            break_money_to_denom(float(string))



if __name__ == "__main__":
    main()