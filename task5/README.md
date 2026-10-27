# Task 5: Repeated Transaction Detection

## Description

This Python program identifies repeated transaction IDs in a list. It uses loops, conditional statements, and list operations to find duplicate transactions and display them.

## Problem Statement

Develop a Python program to process a list of transaction IDs, detect repeated transactions, and display the duplicate IDs without repeating them in the output.

## Objectives

- To understand Python lists and loops.
- To use conditional statements.
- To identify duplicate transaction IDs.
- To use the `count()` method to count occurrences.
- To store and display unique duplicate IDs.

## Assumptions

- Transaction IDs are stored as strings.
- The transaction list may contain duplicate IDs.
- A transaction ID is considered repeated if it occurs more than once.
- Each repeated transaction ID is displayed only once.
- The program uses a predefined list of transactions.

## Algorithm

1. Start.
2. Create a list containing transaction IDs.
3. Initialize an empty list called `duplicates`.
4. Traverse each transaction ID in the transaction list.
5. Check whether the transaction ID occurs more than once.
6. If it occurs more than once, check whether it is already in the `duplicates` list.
7. If it is not already present, add it to the `duplicates` list.
8. Display all transaction IDs.
9. If duplicates exist, display the repeated transaction IDs.
10. Otherwise, display "No repeated transactions found."
11. Stop.

## Flowchart

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/f45ecfa6-dee3-4ffb-b8a1-03839b952b35" />


## Pseudocode

```text
START

SET transactions = list of transaction IDs
SET duplicates = empty list

FOR each transaction in transactions
    IF count of transaction in transactions > 1
        IF transaction not in duplicates
            ADD transaction to duplicates
        END IF
    END IF
END FOR

PRINT all transactions

IF duplicates is not empty
    PRINT repeated transactions
ELSE
    PRINT "No repeated transactions found."
END IF

STOP
```

## Python Source Code

```python
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
```

## Conclusion

This program demonstrates the use of Python lists, loops, conditional statements, and the `count()` method to identify repeated transaction IDs. It displays all transactions and lists each duplicate transaction ID only once. This task helps in understanding basic data handling and duplicate detection in Python.









