# Number Pattern

## 1. Problem Statement

The Number Pattern program is a simple Python program that prints a triangular number pattern based on the number of rows entered by the user.

The program uses nested `for` loops to print numbers from 1 up to the current row number.

## 2. Objectives

- To accept the number of rows from the user.
- To understand the use of `for` loops in Python.
- To understand the use of nested loops.
- To generate a number pattern.
- To validate the user input.

## 3. Features

- Accepts the number of rows as input.
- Validates whether the number of rows is positive.
- Uses nested `for` loops.
- Prints a simple triangular number pattern.
- Displays an error message for invalid input.

## 4. Technologies Used

- Programming Language: Python 3
- IDE: PyCharm
- Concepts Used: Input/Output, Conditional Statements, `for` Loops, and Nested Loops

## 5. How It Works

1. The user enters the number of rows.
2. The program checks whether the number of rows is greater than zero.
3. If the number is less than or equal to zero, an invalid input message is displayed.
4. Otherwise, the outer loop controls the number of rows.
5. The inner loop prints numbers from 1 to the current row number.
6. After each row, the program moves to the next line.
7. The complete number pattern is displayed.

## 6. Algorithm

1. Start.
2. Read the number of rows.
3. Check whether the number of rows is less than or equal to zero.
4. If yes, display "Invalid input! Enter a positive number.".
5. Otherwise, start an outer loop from 1 to the given number of rows.
6. For each row, start an inner loop from 1 to the current row number.
7. Print the current number.
8. Move to the next line after completing each row.
9. Stop.

## 7. Flowchart
<img width="1182" height="1804" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/f51f3e7f-752c-44cb-8abc-1a6ca80061e7" />


## 8. Pseudocode

START

INPUT n

IF n <= 0 THEN
    DISPLAY "Invalid input! Enter a positive number."
ELSE
    FOR i = 1 TO n
        FOR j = 1 TO i
            DISPLAY j
        END FOR
        MOVE TO NEXT LINE
    END FOR
END IF

STOP

## 9. Python Source Code

```python
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
```

## 10. Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| 1 | 1 row | 1 |
| 2 | 3 rows | 1 / 1 2 / 1 2 3 |
| 3 | 4 rows | 1 / 1 2 / 1 2 3 / 1 2 3 4 |
| 4 | 5 rows | Five rows of the number pattern |
| 5 | 0 rows | Invalid input! |

## 11. Sample Input and Output

### Example 1: Three Rows

Input:

```text
Enter number of rows: 3
```

Output:

```text
1
1 2
1 2 3
```

### Example 2: Four Rows

Input:

```text
Enter number of rows: 4
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
```

### Example 3: Invalid Input

Input:

```text
Enter number of rows: 0
```

Output:

```text
Invalid input! Enter a positive number.
```

## 12. Learning Outcomes

Through this project, I learned:

- How to accept user input in Python.
- How to use `for` loops.
- How to use nested loops.
- How to generate patterns using programming logic.
- How to validate user input.

## 13. Conclusion

The Number Pattern program demonstrates the use of nested `for` loops to generate a simple triangular number pattern. It also validates the number of rows entered by the user. This project helped me understand how loops and programming logic can be used to generate patterns in Python.
