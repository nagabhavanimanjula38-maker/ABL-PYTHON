# Number Pattern

print("Number Pattern")

n = int(input("Enter number of rows: "))

if n <= 0:
    print("Invalid input! Enter a positive number.")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        