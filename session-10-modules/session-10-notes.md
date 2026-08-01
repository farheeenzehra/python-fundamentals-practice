# Session 10 - Modules

**Date:** 02 August 2026

---

## Goal

Learn how to use Python's built-in modules to access pre-written functionality instead of writing everything from scratch.

---

## Concepts Covered

- Modules
- `import`
- `math`
- `random`
- `datetime`

---

## What I Learned

- A module is a collection of pre-written Python code that provides useful functions.
- Modules help save time by giving access to functionality that is already built into Python.
- A module must be imported before its functions can be used.
- Different modules are designed for different purposes.

---

## Modules I Used

### `math`

Used for mathematical operations.

Functions practiced:

- `sqrt()`
- `ceil()`
- `floor()`

---

### `random`

Used for generating random values.

Functions practiced:

- `randint()`

---

### `datetime`

Used for working with dates and time.

Function practiced:

- `datetime.datetime.now()`

---

## Things That Clicked

### What does `randint` mean?

**Answer:**

- `rand` = random
- `int` = integer

So `randint()` simply returns a random whole number between two given numbers.

---

### Why do we write `datetime.datetime.now()`?

**Answer:**

- First `datetime` → the module.
- Second `datetime` → the class inside the module.
- `now()` → returns the current date and time.

Flow:

```text
Module → Class → Method
```

---

### Why do we use `import`?

**Answer:**

`import` allows us to use Python's built-in modules without writing those features ourselves.

---

### Choosing the Right Data Structure

While building the mini project, I first thought of storing motivational quotes inside a **list**.

Then I realized that every **lucky number** could have its own corresponding quote.

That made a **dictionary** a much better choice because each number (key) directly points to its matching motivation (value).

This was my first time choosing a data structure based on the problem instead of simply using the one I had recently learned.

---

## Practice Programs

- math.py
- random.py
- datetime.py

---

## Mini Project

**Daily Companion**

Features:

- Show today's date.
- Generate a lucky number.
- Display the motivation assigned to that lucky number.

---

## Skills Gained

- Importing modules.
- Using Python's built-in libraries.
- Performing mathematical operations.
- Generating random numbers.
- Accessing the current date and time.
- Selecting the appropriate data structure for a problem.

---

## Reflection

This session taught me that Python already provides many powerful tools through modules, so I don't always have to build everything from scratch. The biggest takeaway, however, wasn't learning `math`, `random`, or `datetime`—it was realizing that choosing the right data structure depends on the problem I'm solving. That small realization made me feel like I was beginning to think like a programmer rather than just learning Python syntax.