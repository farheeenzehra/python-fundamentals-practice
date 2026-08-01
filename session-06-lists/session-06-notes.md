# Session 06 - Lists

**Date:** 26 July 2026

---

## Goal

Learn how to store and manage multiple values using Python lists.

---

## Concepts Covered

- Lists
- Indexing
- Updating Items
- append()
- insert()
- remove()
- len()
- sort()
- Slicing
- for Loop with Lists

---

## What I Learned

- Lists store multiple values inside one variable.
- List items can be added, updated, removed, and accessed using indexes.
- `append()` adds an item at the end of the list.
- `len()` returns the total number of items.
- Lists are mutable, meaning their contents can be changed.

---

## Things That Clicked

### One List > Many Variables

Earlier, I would've created:

```python
student1
student2
student3
```

Now I understand that one list can store all related values, making programs much cleaner.

---

## Things I Got Confused About

### append() vs insert()

**Answer:**

`append()` always adds at the end.

`insert()` adds at a specific position.

---

### Why doesn't this work?

```python
"Total Students: " + len(students)
```

**Answer:**

Because `len()` returns an integer.

It must be converted to a string using:

```python
str(len(students))
```

---

### Why should the list be outside the while loop?

**Answer:**

If the list is created inside the loop, it gets recreated every iteration and all previous data is lost.

---

## Practice Programs

- Student List Practice
- Shopping List
- Favorite Fruits
- List Operations

---

## Mini Project

Student Management System

---

## Skills Gained

- Managing multiple values.
- Using list methods.
- Traversing lists using loops.
- Building menu-driven programs with lists.

---

## Reflection

This session completely changed how I store data. Instead of creating many separate variables, I learned to group related information into one list. Building the Student Management System helped me connect loops, functions, conditions, and lists together in one real program.