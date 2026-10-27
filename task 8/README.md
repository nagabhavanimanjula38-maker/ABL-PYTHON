# Task 8: Student Marks Analysis

## 1. Problem Statement
Write a Python program to accept marks in three subjects, validate the marks, calculate the average, and display whether the student has passed or failed. A student passes only if they score at least 40 marks in every subject.

## 2. Objectives
- Accept marks in three subjects.
- Validate marks between 0 and 100.
- Calculate the average marks.
- Display Pass or Fail based on the marks obtained.

## 3. Assumptions
- Marks are entered as integers.
- Marks must be between 0 and 100, inclusive.
- A minimum of 40 marks is required in each subject to pass.
- Non-numeric inputs are not handled.

## 4. Algorithm
1. Start.
2. Display the program title.
3. Input marks for three subjects.
4. Check whether any mark is below 0 or above 100.
5. If marks are invalid, display an error message.
6. Otherwise, calculate and display the average.
7. If all three marks are at least 40, display Pass; otherwise, display Fail.
8. Stop.

## 5. Flowchart
<img width="1175" height="1338" alt="image" src="https://github.com/user-attachments/assets/d9c56df3-7b19-4ffa-91b3-633ec08d91b1" />


## 6. Pseudocode
```text
START
INPUT m1, m2, m3

IF any mark < 0 OR any mark > 100
    DISPLAY invalid marks message
ELSE
    average = (m1 + m2 + m3) / 3
    DISPLAY average

    IF m1 >= 40 AND m2 >= 40 AND m3 >= 40
        DISPLAY "Result: Pass"
    ELSE
        DISPLAY "Result: Fail"
    END IF
END IF

STOP
```

## 7. Python Source Code
```python
print("Student Marks Analysis")

m1 = int(input("Enter marks in subject 1 (0-100): "))
m2 = int(input("Enter marks in subject 2 (0-100): "))
m3 = int(input("Enter marks in subject 3 (0-100): "))

if (m1 < 0 or m1 > 100 or
    m2 < 0 or m2 > 100 or
    m3 < 0 or m3 > 100):
    print("Invalid marks! Enter marks between 0 and 100.")
else:
    average = (m1 + m2 + m3) / 3
    print("Average marks:", round(average, 2))

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
```

## 8. Test Cases

| Test | Subject 1 | Subject 2 | Subject 3 | Expected Result |
|---|---:|---:|---:|---|
| 1 | 80 | 75 | 90 | Average: 81.67, Pass |
| 2 | 40 | 40 | 40 | Average: 40.0, Pass |
| 3 | 35 | 80 | 70 | Average: 61.67, Fail |
| 4 | -5 | 70 | 80 | Invalid marks |
| 5 | 90 | 101 | 85 | Invalid marks |

## 9. Sample Output
```text
Student Marks Analysis
Enter marks in subject 1 (0-100): 80
Enter marks in subject 2 (0-100): 75
Enter marks in subject 3 (0-100): 90
Average marks: 81.67
Result: Pass
```

## 10. Conclusion
The program validates marks, calculates the average, and determines whether a student passes based on the minimum marks required in all three subjects.
