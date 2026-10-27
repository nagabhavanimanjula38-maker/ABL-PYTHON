
# Task 5: Repeated Transaction Detection

transactions = ["T101", "T102", "T103", "T101", "T104", "T102"]
duplicates = []

for transaction in transactions:
    if transactions.count(transaction) > 1:
        if transaction not in duplicates:
            duplicates.append(transaction)

print("All Transactions:", transactions)

if duplicates:
    print("Repeated Transactions:", duplicates)
else:
    print("No repeated transactions found.")
