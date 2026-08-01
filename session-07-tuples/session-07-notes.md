# Session 07 — Tuples

**Date:** 31 July 2026

---

##  Goal

Understand tuples and learn when to use them instead of lists.

---

##  What I Actually Learned

- Tuples use `()` while lists use `[]`.
- Tuples are immutable, meaning their values cannot be changed.
- Most things I already knew from lists also work with tuples:
  - Indexing
  - `for` loop
  - `len()`
  - `in`
  - `.index()`
- The biggest difference is that tuples are for data that should stay fixed, we cannot modify them.

---

##  Things I Got Confused About

### Printing every element

At first I thought I had to write:

```python
print(tuple[0])
print(tuple[1])
print(tuple[2])
...
```

Then I realized I can simply use:

```python
for item in tuple:
    print(item)
```

---

### Value vs Index

I got confused because of this:

```python
for country in countries:
```

I thought `country` was the index.

Later I understood:

- `country` = actual value
- `countries.index(country)` = position of that value

---

### Menu-based Programs

I also understood why the selected option wasn't changing.
Because I wasn't calling the menu function again inside the loop.
The menu must be displayed after every completed operation.

---

##  What I Practiced

- Creating tuples.
- Accessing elements using indexes.
- Looping through tuples.
- Finding tuple length.
- Searching using `in`.
- Finding position using `.index()`.

---

##  Mini Project

### Country Information System

Features:

- Display all countries.
- Search country.
- Show statistics.
- Exit.

Concepts revised:

- Functions
- While Loop
- If-Elif
- Tuples
- Loops
- Searching

---

##  Personal Reflection

Today's session felt easier because tuples are very similar to lists.

Most of my confusion wasn't about tuples themselves.

It was about understanding the difference between **values and indexes** and recognizing the programming pattern used in menu-driven programs.

I also realized that I should stop thinking about individual lines of code and start thinking about the overall structure of a program first.