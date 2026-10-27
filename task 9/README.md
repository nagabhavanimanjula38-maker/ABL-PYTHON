# Parking Fee Calculator

## 1. Problem Statement

The Parking Fee Calculator is a simple Python program that calculates the parking fee based on the number of hours a vehicle is parked.

The program accepts the parking duration as input, validates the entered value, and calculates the parking fee according to the given parking rates.

## 2. Objectives

- To accept the number of parking hours from the user.
- To validate the parking hours.
- To calculate the parking fee using conditional statements.
- To display the calculated parking fee.
- To understand the practical use of `if` and `else` statements in Python.

## 3. Features

- Accepts parking hours as input.
- Validates whether the entered hours are valid.
- Charges Rs. 20 for the first two hours.
- Charges Rs. 10 for every additional hour.
- Displays the total parking fee.
- Displays an error message for invalid input.

## 4. Technologies Used

- Programming Language: Python 3
- IDE: PyCharm
- Concepts Used: Input/Output, Arithmetic Operators, Conditional Statements, and Input Validation

## 5. How It Works

1. The user enters the number of parking hours.
2. The program checks whether the entered hours are greater than zero.
3. If the hours are less than or equal to zero, an invalid input message is displayed.
4. If the parking duration is up to two hours, the fee is Rs. 20.
5. If the parking duration is more than two hours, Rs. 10 is added for every additional hour.
6. The final parking fee is displayed.

## 6. Algorithm

1. Start.
2. Read the number of parking hours.
3. Check whether the hours are less than or equal to zero.
4. If yes, display "Invalid hours!".
5. Otherwise, check whether the hours are less than or equal to two.
6. If yes, set the fee to Rs. 20.
7. Otherwise, calculate the fee using:

   Parking Fee = 20 + (Hours - 2) × 10

8. Display the parking fee.
9. Stop.

## 7. Flowchart


## 8. Pseudocode

START

INPUT hours

IF hours <= 0 THEN
    DISPLAY "Invalid hours!"
ELSE
    IF hours <= 2 THEN
        fee = 20
    ELSE
        fee = 20 + (hours - 2) * 10
    END IF

    DISPLAY "Parking fee: Rs.", fee
END IF

STOP

## 9. Formula Used

For parking up to 2 hours:

Parking Fee = Rs. 20

For parking more than 2 hours:

Parking Fee = 20 + (Hours - 2) × 10

## 10. Python Source Code

```python
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
```

## 11. Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| 1 | 1 hour | Parking fee: Rs. 20 |
| 2 | 2 hours | Parking fee: Rs. 20 |
| 3 | 4 hours | Parking fee: Rs. 40 |
| 4 | 6 hours | Parking fee: Rs. 60 |
| 5 | 0 hours | Invalid hours! |

## 12. Sample Input and Output

### Example 1: Parking for 2 Hours

Input:

```text
Enter parking hours: 2
```

Output:

```text
Parking fee: Rs. 20
```

### Example 2: Parking for 5 Hours

Input:

```text
Enter parking hours: 5
```

Output:

```text
Parking fee: Rs. 50
```

### Example 3: Invalid Input

Input:

```text
Enter parking hours: 0
```

Output:

```text
Invalid hours!
```

## 13. Learning Outcomes

Through this project, I learned:

- How to accept user input in Python.
- How to use arithmetic operations.
- How to use `if` and `else` statements.
- How to validate user input.
- How to apply conditional logic to solve a real-world problem.

## 14. Conclusion

The Parking Fee Calculator is a simple Python program that calculates the parking fee based on the number of hours a vehicle is parked. It demonstrates the use of input/output statements, arithmetic operations, conditional statements, and input validation. This project helped me understand how Python can be used to solve simple real-world problems.
