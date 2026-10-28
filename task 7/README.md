# Traffic Violation Penalty Calculator

## 1. Problem Statement
Develop a Python program to calculate traffic violation fines based on the type and number of violations committed.

## 2. Objectives
- To understand conditional statements in Python.
- To use loops for repeated inputs.
- To calculate the total fine for multiple violations.

## 3. Assumptions
- No helmet fine: ₹500.
- Signal jumping fine: ₹1000.
- No driving licence fine: ₹2000.
- These fine amounts are sample values for this assignment.

## 4. Algorithm
1. Start the program.
2. Read the number of violations.
3. Check whether the number is valid.
4. Display the available violation types and fines.
5. Read the violation type.
6. Calculate the fine based on the selected type.
7. Add the fine to the total fine.
8. Repeat until all violations are processed.
9. Display the total fine.
10. Stop the program.

## 5. Flowchart
<img width="1820" height="1596" alt="mermaid-diagram (6)" src="https://github.com/user-attachments/assets/4775acca-5878-4f2b-8ebd-1d25da1bac3b" />


## 6. Pseudocode
```text
START
INPUT number_of_violations

IF number_of_violations <= 0
    PRINT "Invalid number of violations"
ELSE
    total_fine = 0
    REPEAT for each violation
        DISPLAY violation types
        INPUT choice

        IF choice = 1
            fine = 500
        ELSE IF choice = 2
            fine = 1000
        ELSE IF choice = 3
            fine = 2000
        ELSE
            PRINT "Invalid violation type"
            CONTINUE
        END IF

        total_fine = total_fine + fine
    END REPEAT

    PRINT total_fine
END IF
STOP
```

## 7. Python Source Code
```python
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
```

## 8. Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| 1 | 1 violation, choice 1 | Total fine: ₹500 |
| 2 | 1 violation, choice 2 | Total fine: ₹1000 |
| 3 | 2 violations, choices 1 and 3 | Total fine: ₹2500 |
| 4 | Number of violations = 0 | Invalid number of violations |

## 9. Sample Output
```text
Traffic Violation Penalty Calculator
Enter number of violations: 2

1. No helmet - Rs. 500
2. Signal jumping - Rs. 1000
3. No driving licence - Rs. 2000
Enter violation type (1-3): 1
Fine: Rs. 500

1. No helmet - Rs. 500
2. Signal jumping - Rs. 1000
3. No driving licence - Rs. 2000
Enter violation type (1-3): 3
Fine: Rs. 2000

Total fine: Rs. 2500
```

## 10. Conclusion
This program demonstrates the use of loops, conditional statements, and arithmetic operations to calculate the total traffic violation fine.
