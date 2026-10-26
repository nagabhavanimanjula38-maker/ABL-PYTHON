
# withdraw balance
balance = 10000
withdraw = int(input('Enter withdraw amount: '))

if withdraw <= balance and withdraw > 0:
    print("Success! balance remaining:", balance - withdraw)
else:
    print("No Balance!")
