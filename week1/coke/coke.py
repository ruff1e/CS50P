amountDue = 50

while amountDue > 0 :
    print(f"Amount Due: {amountDue}")
    insertCoin = int(input("Insert Coin: "))

    if insertCoin in [5,10,25]:
        amountDue -= insertCoin

change = abs(amountDue)
print(f"Change Owed: {change}")