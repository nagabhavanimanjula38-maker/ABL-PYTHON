# Task 4: Password Creation

## Description

This Python program checks the strength of a password based on its length and character types. It checks for uppercase letters, lowercase letters, digits, and special characters to calculate a password strength score.

## Problem Statement

Develop a Python program to validate a password and classify its strength as Weak, Medium, or Strong based on predefined criteria.

## Objectives

- To understand loops and conditional statements in Python.
- To check uppercase and lowercase letters.
- To identify digits and special characters.
- To calculate a password strength score.
- To identify common or easily guessed passwords.

## Assumptions

- A password should contain at least 8 characters.
- Uppercase letters, lowercase letters, digits, and special characters contribute to the score.
- The special characters checked are `@`, `#`, `$`, `!`, `%`, and `*`.
- Passwords containing `123` or the word `password` are rejected.
- The maximum score is 5.

## Algorithm

1. Start.
2. Read the password from the user.
3. Initialize the character-checking flags to False.
4. Check each character for uppercase, lowercase, digits, and special characters.
5. Initialize the score to zero.
6. Increase the score for each satisfied criterion.
7. If the password contains `123` or `password`, display an easy-password warning.
8. Otherwise, if the password has fewer than 8 characters, display a length warning.
9. Otherwise, display the score out of 5.
10. Classify the password as Weak, Medium, or Strong.
11. Stop.

## Flowchart

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/ed00209b-d2f2-466f-a1b9-b2a4a9e14108" />


## Pseudocode

```text
START
INPUT password

SET has_upper = False
SET has_lower = False
SET has_digit = False
SET has_special = False

FOR each character in password
    CHECK uppercase, lowercase, digit, and special character
END FOR

SET score = 0

IF length >= 8
    score = score + 1
IF has_upper
    score = score + 1
IF has_lower
    score = score + 1
IF has_digit
    score = score + 1
IF has_special
    score = score + 1

IF password contains "123" OR "password"
    PRINT "Fail - Avoid easy passwords!"
ELSE IF length < 8
    PRINT "Fail - Password must have at least 8 characters."
ELSE
    PRINT score out of 5

    IF score <= 2
        PRINT "WEAK Password"
    ELSE IF score <= 4
        PRINT "MEDIUM Password"
    ELSE
        PRINT "STRONG Password"
    END IF
END IF

STOP
```

## Test Cases

| Password | Expected Result |
|---|---|
| `Abcdef1!` | Score: 5/5 — STRONG |
| `abcdef12` | Score: 3/5 — MEDIUM |
| `abcdefgh` | Score: 2/5 — WEAK |
| `abc12345` | Fail — Avoid easy passwords! |
| `Ab1!` | Fail — Password must have at least 8 characters. |
| `PASSWORD1!` | Fail — Avoid easy passwords! |

## Conclusion

This program demonstrates the use of loops, Boolean variables, and conditional statements to validate a password and estimate its strength based on five criteria.
