
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
amount = sys.argv[1]
Amount = float(amount)
z = int(((Amount-int(Amount))+0.001) * 100)
bills_denominations(int(Amount))
coins_denominations(z)

# note:  same code, in the first version that was submitted it gives correct output
# when I use sys.argv the coding give different results!!!!!!!!!!!!!!

#(venv) C:\Users\PC\python_work\November_04>money_denominat.py 123.45
#(24, 'fives')
#(3, 'ones')
#(9, 'nickles')

#(venv) C:\Users\PC\python_work\November_04>money_denominat.py 2345.67
#(469, 'fives')
#(13, 'nickles')
#(2, 'pennies')













