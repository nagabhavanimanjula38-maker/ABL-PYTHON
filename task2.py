# Electricity bill
units = int(input("Enter Current units: "))

if units < 0:
    print("Invalid units!")
elif units <= 100:
    bill = units * 5
    print("Your bill:", bill)
else:
    bill = 500 + (units - 100) * 7
    print("Your bill:", bill)
