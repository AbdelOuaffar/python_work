
import sys
def coins_denominations(amount):
    coins = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}
    for key in coins:
        coin = amount // coins[key]
        k = amount % coins[key]
        amount = k
        if coin != 0:
           print(coin, key)
def bills_denominations(amount):

    bills = {"hundreds": 100, "twenties": 20, "tens": 10, "fives": 5, "twos": 2, "ones": 1}
    for key in bills:
        bill = amount // bills[key]
        r = amount % bills[key]
        amount = r
        if bill != 0:
            print(bill, key)
def main():
    try:
        char_seq1 = ""
        char_seq2 = ""
        string = sys.argv[1]
        for char in string:

            if char != ".":
                char_seq1 += char
            elif char == ".":

                char_seq2 = char_seq1
                char_seq1 = ""

        bills_denominations(int(char_seq2))
        coins_denominations(int(char_seq1))
    except TypeError:
        print("type error")
if __name__== "__main__":
    main()

#(venv) C:\Users\PC\python_work\November_04>money_denominat.py 234.99
#(46, 'fives')
#(4, 'ones')
#(19, 'nickles')
#(4, 'pennies')












