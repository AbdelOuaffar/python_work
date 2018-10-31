
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
amount = input("enter the amount  :")
Amount = float(amount)
z = int(((Amount-int(Amount))+0.001) * 100)
bills_denominations(int(Amount))
coins_denominations(z)
#Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
#runfile('C:/Users/PC/python_work/November_04/money_denominat.py', wdir='C:/Users/PC/python_work/November_04')
#enter the amount  :>? 123.45
#1 hundreds
#1 twenties
#1 twos
#1 ones
#1 quarters
#2 dimes













