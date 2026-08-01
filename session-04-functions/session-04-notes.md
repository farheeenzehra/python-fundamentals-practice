# Session 04 - Functions

**Date:** 23 July 2026

---

## Goal

Understand how functions organize code, avoid repetition, and make programs easier to build.

---

## Concepts Covered

- Functions
- def
- Function Calling
- return
- Code Reusability

---

## What I Learned

- A function is a reusable block of code that performs one specific task.
- Functions are created using the `def` keyword.
- A function only executes when it is called.
- `return` sends a value back to the place where the function was called.
- Functions make programs shorter, cleaner, and easier to manage.

---

### return Finally Made Sense

I was confused about statements like:

```python
choice = menu()
```

Later I understood the flow:

1. `menu()` runs.
2. It reaches `return choice`.
3. That returned value gets stored in the variable `choice`.

The assignment doesn't call the function—the parentheses `()` do.

---
## Things That Clicked

### One Function = One Job

Instead of making one huge function, I learned that each function should have one clear responsibility.

This makes programs much more organized.

### Creating a function vs calling a function

**Answer:**  
`def` only creates the function. The function runs only when it is called using `function_name()`.

---

### Why do we use `return`?

**Answer:**  
`return` sends a value back from the function so it can be used somewhere else in the program.

---

### How does `choice = menu()` work?

**Answer:**  
Python first executes `menu()`, gets the returned value, and then stores that value inside `choice`.

---

### Why create functions instead of writing everything directly?

**Answer:**  
Functions divide one large problem into smaller tasks, making programs cleaner, easier to debug, and reusable.

---

## Practice Programs

- Student Result Using Functions
- Bank Account Checker
- Simple Calculator Using Functions

---

## Mini Project

Bank Management System

---

## Skills Gained

- Creating functions.
- Calling functions.
- Returning values.
- Organizing code into smaller parts.
- Reusing code instead of repeating it.
- Writing cleaner programs.

---

## Reflection

This session completely changed how I structure programs. Before learning functions, I wrote everything in one long block of code. After practicing, I realized that functions are not just a Python feature—they are a way of organizing my thinking. They became the foundation for the menu-driven programs I built later.