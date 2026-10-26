
# Task 1: Withdraw Balance

balance = 10000

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid withdrawal amount!")
elif withdraw > balance:
    print("Insufficient balance!")
else:
    balance = balance - withdraw
    print("Withdrawal successful!")
    print("Remaining balance:", balance)
