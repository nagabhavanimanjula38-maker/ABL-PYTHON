# Parking Fee Calculator

print("Parking Fee Calculator")

hours = int(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid hours!")
else:
    if hours <= 2:
        fee = 20
    else:
        fee = 20 + (hours - 2) * 10

    print("Parking fee: Rs.", fee)
    