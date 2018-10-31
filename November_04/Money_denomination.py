coins={"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}
def coins_denominations(amount):
    for key in coins:
        m = amount // coins[key]
        r = amount % coins[key]
        print (m,r)
coins_denominations(8)




























coins_denominations(80)






















print(coins_denominations(99))

