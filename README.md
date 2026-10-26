# Task 1: Withdrawal Balance System

## Description
This Python program simulates a bank withdrawal system by checking the withdrawal amount and available balance.

## Problem Statement
Develop a Python program to withdraw money from an account with an initial balance of ₹10,000.

## Objectives
- To understand conditional statements.
- To validate the withdrawal amount.
- To calculate the remaining balance.

## Assumptions
- The initial balance is ₹10,000.
- The withdrawal amount must be positive.
- The withdrawal amount must not exceed the available balance.

## Algorithm
1. Start.
2. Set balance to 10000.
3. Read the withdrawal amount.
4. Check whether the amount is valid.
5. Check whether sufficient balance is available.
6. If valid, subtract the withdrawal amount from the balance.
7. Display the result and remaining balance.
8. Stop.

## Pseudocode
```text
START
balance = 10000
INPUT withdraw

IF withdraw <= 0
    PRINT "Invalid withdrawal amount"
ELSE IF withdraw > balance
    PRINT "Insufficient balance"
ELSE
    balance = balance - withdraw
    PRINT "Withdrawal successful"
    PRINT balance
END IF

STOP
```

## Test Cases

| Withdrawal Amount | Expected Output |
|---:|---|
| 2000 | Remaining balance: 8000 |
| 12000 | Insufficient balance |
| 0 | Invalid withdrawal amount |
| -500 | Invalid withdrawal amount |

## Conclusion
This program demonstrates the use of Python variables, arithmetic operations, and conditional statements to simulate a bank withdrawal system.
