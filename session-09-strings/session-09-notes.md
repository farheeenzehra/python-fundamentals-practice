# Session 09 - Strings

**Date:** 1 August 2026

---

## Goal

Understand how to access, manipulate, search, and modify text using Python Strings.

---

## Concepts Covered

- Strings
- String Indexing
- String Slicing
- String Methods
- Searching in Strings

---

## What I Learned

- A string is a sequence of characters.
- Every character in a string has an index.
- Spaces are also counted as characters.
- Indexing is used to access a single character.
- Slicing is used to access a part of a string.
- String methods return a **new string** instead of changing the original one.

---

## Things That Clicked

### Spaces also have indexes

I got confused when:

```python
name = "  Farheen Zehra"

print(name.find("e"))
```

returned `6` instead of `4`.

**Answer:**

Python counts **every character**, including spaces.

```
"  Farheen Zehra"

0 -> space
1 -> space
2 -> F
3 -> a
4 -> r
5 -> h
6 -> e
```

So the first `e` is actually at index `6`.

---

### Why didn't `replace()` change my original string?

I noticed that:

```python
text.replace("Python", "AI")
```

didn't permanently change the string.

**Answer:**

Strings are **immutable**.

Methods like:

- `replace()`
- `upper()`
- `lower()`
- `title()`

return a **new string**.

If I want to save the change, I must write:

```python
text = text.replace("Python", "AI")
```

---

### Indexing vs Slicing

**Indexing**

Returns one character.

```python
name[0]
```

**Slicing**

Returns part of the string.

```python
name[0:7]
```

---

### `find()` vs `count()`

`find()`

Returns the index where the text first appears.

```python
text.find("Python")
```

`count()`

Returns how many times the text appears.

```python
text.count("Python")
```

---

## Practice Programs

- String Indexing
- String Slicing
- String Methods
- Search and Replace

---

## Mini Project

Text Analyzer

---

## Skills Gained

- Accessing characters using indexing.
- Extracting text using slicing.
- Using common string methods.
- Searching inside strings.
- Replacing text.
- Building my first menu-driven string application.

---

## Reflection

This session showed me that strings are much more than plain text. I learned how Python treats every character individually and how powerful built-in string methods are. The biggest realization was that strings cannot be changed directly—they always create a new string. Building the Text Analyzer helped me combine everything I learned into one practical program.