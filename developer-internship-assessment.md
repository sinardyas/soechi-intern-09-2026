# Developer Internship Assessment (Early Year)

> **Audience:** 1st–2nd year Computer Science / Informatics / IT students
> **Format:** Quiz, Parts 1–4 (≈ 90 minutes, supervised)
> **Language:** Candidates may answer coding questions in **any language** (Python, JavaScript/TypeScript, Java, Go, C#, PHP, etc.) unless stated otherwise.

---

## Table of Contents

1. [Instructions for Candidates](#instructions-for-candidates)
2. [Part 1 — Multiple Choice (20 pts)](#part-1--multiple-choice-20-pts)
3. [Part 2 — Short Answer Theory (21 pts)](#part-2--short-answer-theory-21-pts)
4. [Part 3 — Code Reading & Debugging (20 pts)](#part-3--code-reading--debugging-20-pts)
5. [Part 4 — Live Coding Exercises (39 pts)](#part-4--live-coding-exercises-39-pts)

---

## Instructions for Candidates

- Read each question carefully. Partial answers still earn points — show your reasoning.
- You may **not** use AI assistants or search engines during this quiz.
- For coding questions, correctness matters most, then readability. Comments explaining your approach are welcome.
- If a question is unclear, write down your assumption and continue.

---

## Part 1 — Multiple Choice (20 pts)

*2 points each. Choose one answer.*

**1.1** What is the time complexity of **binary search** on a sorted array of `n` elements?

- a) O(1)
- b) O(log n)
- c) O(n)
- d) O(n log n)

**1.2** Which data structure follows **Last In, First Out (LIFO)**?

- a) Queue
- b) Stack
- c) Linked List
- d) Hash Map

**1.3** An HTTP response with status code **404** means:

- a) Internal server error
- b) Unauthorized
- c) Resource not found
- d) Request successful, no content

**1.4** Which HTTP method is conventionally used to **create** a new resource in a REST API?

- a) GET
- b) POST
- c) DELETE
- d) HEAD

**1.5** Which SQL statement removes **specific rows** matching a condition, while keeping the table?

- a) `DROP TABLE`
- b) `DELETE FROM ... WHERE ...`
- c) `TRUNCATE TABLE`
- d) `ALTER TABLE`

**1.6** Which Git command **creates a new branch and switches to it**?

- a) `git branch -d feature`
- b) `git merge feature`
- c) `git checkout -b feature`
- d) `git push origin feature`

**1.7** Which of the following is **NOT** one of the core principles of Object-Oriented Programming?

- a) Encapsulation
- b) Inheritance
- c) Polymorphism
- d) Compilation

**1.8** What is the main purpose of a **primary key** in a relational database table?

- a) To encrypt the row
- b) To uniquely identify each row
- c) To sort the table automatically
- d) To link to a file on disk

**1.9** What is the **average** time complexity of looking up a key in a hash map / dictionary?

- a) O(1)
- b) O(log n)
- c) O(n)
- d) O(n²)

**1.10** Which of the following is **valid JSON**?

- a) `{name: "Budi", age: 21}`
- b) `{'name': 'Budi', 'age': 21}`
- c) `{"name": "Budi", "age": 21}`
- d) `{"name": "Budi", "age": 21,}`

---

## Part 2 — Short Answer Theory (21 pts)

*3 points each. Answer in 2–5 sentences. Examples are encouraged.*

**2.1** What is the difference between a **process** and a **thread**?

**2.2** Compare **SQL (relational)** and **NoSQL** databases. Give one situation where you would choose each.

**2.3** What is an **API**? What makes an API "RESTful"? Name at least two characteristics.

**2.4** Describe, at a high level, what happens when you type `https://www.example.com` into a browser and press Enter.

**2.5** Why do developers write **unit tests**? What makes a unit test "good"?

**2.6** What is a **merge conflict** in Git, why does it happen, and how do you resolve one?

**2.7** A user reports a bug that you **cannot reproduce** on your machine. Describe the steps you would take to investigate.

---

## Part 3 — Code Reading & Debugging (20 pts)

*4 points each.*

### 3.1 — Predict the output (Python)

```python
def f(items):
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result

print(f([1, 2, 3]))
```

a) What is printed?
b) Describe in one sentence what `f` does. Can you write it in one line?

### 3.2 — Predict the output (Python)

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
```

a) What is printed on each line?
b) Is this likely the intended behavior? If not, how would you fix it?

### 3.3 — Predict the output (JavaScript)

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

a) What is logged to the console?
b) Change **one word** so that it logs `0 1 2`. Explain why it works.

### 3.4 — Find the bug

```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

a) Under what input does this function fail? What error occurs?
b) Rewrite the function to handle that case sensibly.

### 3.5 — Write a SQL query

Given these tables:

```
employees(id, name, dept_id, salary)
departments(id, name)
```

Write a query that returns **each department's name and average salary**, but **only for departments with more than 3 employees**, sorted from **highest to lowest** average salary.

---

## Part 4 — Live Coding Exercises (39 pts)

*13 points each. Use any language. Include at least 2 example test cases per exercise showing input → expected output.*

Scoring per exercise: correctness (6) · edge cases (3) · readability & naming (2) · complexity awareness (2)

### 4.1 — Reverse the Words

Write a function that reverses the **order of words** in a sentence. Extra spaces between words should be collapsed into one, and leading/trailing spaces removed.

```
Input:  "  the ship   sails at dawn "
Output: "dawn at sails ship the"
```


### 4.2 — Balanced Brackets

Write a function that returns `true` if a string's brackets `()`, `[]`, `{}` are **balanced and correctly nested**, otherwise `false`. Other characters are ignored.

```
"(a[b]{c})"  -> true
"([)]"       -> false
"(("         -> false
""           -> true
```

*Question: what is the time and space complexity of your solution?*

### 4.3 — Top-N Word Frequency

Write a function `top_words(text, n)` that returns the `n` most frequent words in `text`.

- Case-insensitive (`"The"` and `"the"` are the same word)
- Ignore punctuation `. , ! ? ; :`
- If two words have the same count, sort them alphabetically

```
text = "The cat and the hat. The cat sat!"
top_words(text, 2)  ->  [("the", 3), ("cat", 2)]
```

---
