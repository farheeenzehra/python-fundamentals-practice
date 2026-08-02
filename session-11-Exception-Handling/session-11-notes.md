# Session 11 - Exception Handling

**Date:** 02 August 2026

---

# Goal

Learn how to prevent programs from crashing when users enter invalid input.

---

# Concepts Covered

- Exceptions
- try
- except
- ValueError
- ZeroDivisionError

---

# What I Learned

- An exception is an error that occurs while a program is running.
- Without exception handling, Python immediately stops the program when an error occurs.
- Exception handling allows the program to continue running instead of crashing.
- The risky code is placed inside a `try` block.
- If an error occurs, Python jumps to the matching `except` block.

---

# Exception Handling Structure

```python
try:
    # Risky code

except ErrorType:
    # Handle the error
```

---

# Exceptions I Learned

## ValueError

Occurs when Python receives a value of the correct type but in an invalid format.

Example:

```text
Enter age:
hello
```

```python
int("hello")
```

↓

```text
ValueError
```

---

## ZeroDivisionError

Occurs when dividing a number by zero.

Example:

```python
10 / 0
```

↓

```text
ZeroDivisionError
```

---

# Things That Clicked

### Why use `try`?

Instead of letting the program crash, Python first tries to execute the code.

---

### Why use `except`?

If an error happens inside `try`, Python immediately executes the matching `except` block.

---

### Why specify `ValueError`?

Instead of catching every possible error, it's better to catch only the error you're expecting.

This makes the code cleaner and more professional.

---

### One Design Lesson

I realized that not every part of the program should be inside a `try` block.

Only the code that is actually risky should be handled.

---

# Practice Programs

- exception_handling.py
- multiple_exceptions.py

---

# Mini Project

## MP11 - Safe Calculator

Features:

- Addition
- Subtraction
- Multiplication
- Division
- Exception handling
- Menu-driven program

Errors handled:

- Invalid numeric input
- Division by zero

---

# Skills Gained

- Preventing program crashes
- Handling invalid user input
- Handling division by zero
- Using multiple `except` blocks
- Writing more user-friendly programs

---

# Reflection

This session completely changed how I think about user input.

Earlier, I focused only on making my program work when the user entered the correct values.

Now I also think about what happens when the user enters something unexpected.

Instead of allowing the program to crash, I can guide the user with a meaningful message and keep the program running.

It made my programs feel much closer to real software instead of simple practice exercises.