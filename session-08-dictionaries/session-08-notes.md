# Session 08 - Dictionaries

**Date:** 1 August 2026

---

## Goal

Understand how dictionaries store data using **key-value pairs**, and learn how to access, update, search, traverse, and remove information.

---

## Concepts Covered

- Dictionaries
- Key-Value Pairs
- Accessing Values
- Updating Values
- Adding New Keys
- Searching Keys
- Traversing Dictionaries
- Deleting Dictionary Items

---

## What I Learned

- A dictionary stores data using **keys** instead of indexes.
- Values are accessed using their corresponding key.
- Existing values can be updated.
- New key-value pairs can be added anytime.
- `in` checks whether a **key** exists in the dictionary.
- `del` removes a key and its value.
- A `for` loop traverses a dictionary one key at a time.

---

## Things That Clicked

### One Dictionary = One Object

At first, I wondered if one dictionary could store information for multiple students.

I realized that **one dictionary usually represents one object** (one student, one car, one book, etc.).

If I want to store multiple students, I'll use **a list of dictionaries**, not one huge dictionary.

---

### Lists vs Dictionaries

Lists store values using **indexes**.

```python
students[0]
```

Dictionaries store values using **keys**.

```python
student["name"]
```

This is the biggest conceptual difference between the two.

---

### Traversing a Dictionary

I was confused about how this works:

```python
for key in student:
```

I thought one variable (`key`) couldn't print everything.

Later I understood that the loop automatically changes `key` during each iteration.

For example:

- First iteration → `"name"`
- Second iteration → `"age"`
- Third iteration → `"city"`

Then:

```python
student[key]
```

returns the value for the current key.

---

### Variable vs String

This confused me the most.

Wrong:

```python
student["key"]
```

Correct:

```python
student[key]
```

**Answer:**

- `"key"` is just a string.
- `key` is a variable whose value changes during every loop iteration.

---

### Searching in Dictionaries

I noticed something different from lists.

For lists:

```python
if search in students:
```

checks **values**.

For dictionaries:

```python
if search in student:
```

checks **keys**.

---

## Practice Programs

- Student Dictionary
- Updating Dictionary Information
- Search and Traverse Dictionary

---

## Mini Project

Student Profile Management System

---

## Skills Gained

- Creating dictionaries.
- Accessing values using keys.
- Updating existing values.
- Adding new key-value pairs.
- Searching keys.
- Traversing dictionaries using loops.
- Removing dictionary items.
- Building a menu-driven program using dictionaries.

---

## Reflection

This session changed how I think about storing related information. Lists are useful for storing many values, but dictionaries make data much more meaningful because every value has a name (key). The biggest thing that clicked was understanding how dictionary traversal works and the difference between using a variable (`student[key]`) and a string (`student["key"]`). I also realized that real programs often use **lists of dictionaries**, which is how multiple objects are stored together.