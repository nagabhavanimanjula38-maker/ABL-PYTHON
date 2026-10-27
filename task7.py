# Traffic Violation Penalty Calculator

print("Traffic Violation Penalty Calculator")

n = int(input("Enter number of violations: "))

if n <= 0:
    print("Invalid number of violations!")
else:
    total_fine = 0

    for i in range(n):
        print("\n1. No helmet - Rs. 500")
        print("2. Signal jumping - Rs. 1000")
        print("3. No driving licence - Rs. 2000")

        choice = int(input("Enter violation type (1-3): "))

        if choice == 1:
            fine = 500
        elif choice == 2:
            fine = 1000
        elif choice == 3:
            fine = 2000
        else:
            print("Invalid violation type!")
            continue

        print("Fine: Rs.", fine)
        total_fine += fine

    print("\nTotal fine: Rs.", total_fine)
    