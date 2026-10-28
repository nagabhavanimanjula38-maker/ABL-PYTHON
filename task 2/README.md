# Task 2: Electricity Bill Calculator

## Description
This Python program calculates an electricity bill based on the number of units consumed.

## Problem Statement
Develop a Python program to calculate an electricity bill using the number of units consumed.

## Objectives
- To understand conditional statements in Python.
- To calculate the electricity bill.
- To validate the number of units entered.

## Assumptions
- The number of units cannot be negative.
- The charge is ₹5 per unit for the first 100 units.
- For units above 100, the first 100 units cost ₹500, and each additional unit costs ₹7.

## Algorithm
1. Start.
2. Read the number of electricity units.
3. Check whether the units are negative.
4. If the units are negative, display "Invalid units!".
5. If the units are 100 or less, calculate the bill at ₹5 per unit.
6. Otherwise, calculate ₹500 for the first 100 units and ₹7 for each additional unit.
7. Display the electricity bill.
8. Stop.

## Flowchart
<img width="904" height="1082" alt="mermaid-diagram (3)" src="https://github.com/user-attachments/assets/c7296c6a-9c34-4fe1-9028-78a6b3515b62" />


## Pseudocode
```text
START
INPUT units

IF units < 0
    PRINT "Invalid units!"
ELSE IF units <= 100
    bill = units * 5
    PRINT "Your bill:", bill
ELSE
    bill = 500 + (units - 100) * 7
    PRINT "Your bill:", bill
END IF

STOP
```

## Test Cases

| Units Consumed | Expected Output |
|---:|---|
| 50 | Your bill: 250 |
| 100 | Your bill: 500 |
| 150 | Your bill: 850 |
| -10 | Invalid units! |

## Conclusion
This program demonstrates the use of variables, arithmetic operations, and conditional statements to calculate an electricity bill based on units consumed.
