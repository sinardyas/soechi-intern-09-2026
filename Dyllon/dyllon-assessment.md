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

- b) O(log n)

**1.2** Which data structure follows **Last In, First Out (LIFO)**?

- b) Stack

**1.3** An HTTP response with status code **404** means:

- c) Resource not found

**1.4** Which HTTP method is conventionally used to **create** a new resource in a REST API?

- b) POST

**1.5** Which SQL statement removes **specific rows** matching a condition, while keeping the table?

- b) `DELETE FROM ... WHERE ...`

**1.6** Which Git command **creates a new branch and switches to it**?

 c) `git checkout -b feature`

**1.7** Which of the following is **NOT** one of the core principles of Object-Oriented Programming?

- d) Compilation

**1.8** What is the main purpose of a **primary key** in a relational database table?

- b) To uniquely identify each row

**1.9** What is the **average** time complexity of looking up a key in a hash map / dictionary?

- a) O(log 1)

**1.10** Which of the following is **valid JSON**?

- c) `{"name": "Budi", "age": 21}`

---

## Part 2 — Short Answer Theory (21 pts)

*3 points each. Answer in 2–5 sentences. Examples are encouraged.*

**2.1** What is the difference between a **process** and a **thread**?
a process is a program that is being run, while thread is a single part of a process that contibutes to the completion of a process.
Example of this is game. A game is a wholesome of process while inside the process can involve several threads that do different things like graphics, music, etc. 

**2.2** Compare **SQL (relational)** and **NoSQL** databases. Give one situation where you would choose each.
SQL databases are relational databases that store structured data in tables with rows and columns, and they use relationships between tables. NoSQL databases use models such as documents, key-value pairs, graphs or wide columns and are often more flexible with data structure. I would use SQL for something like banking data where relationships and consistency are important, and NoSQL for something like a large-scale application storing flexible user documents.

**2.3** What is an **API**? What makes an API "RESTful"? Name at least two characteristics.
An API (Application Programming Interface) is an interface that allows different software systems to communicate and exchange data. A RESTful API is an API that follows REST principles, commonly using HTTP methods such as GET, POST, PUT/PATCH and DELETE. Resources are usually identified using URLs, and requests are generally stateless.

**2.4** Describe, at a high level, what happens when you type `https://www.example.com` into a browser and press Enter.
the browser will read the address and uses DNS to search the server and it will also create a secure HTTPS connection on that server. It will send a request to the page and continued with the server that sends back a response in files and the browser will read the files and displays them on the page.

**2.5** Why do developers write **unit tests**? What makes a unit test "good"?
unit tests is done too check whether the code runs as expected or there are errors.
unit tests considered well done if the result stays the same with the same input.

**2.6** What is a **merge conflict** in Git, why does it happen, and how do you resolve one?
A merge conflict occurs when two branches modify the same part of a file and Git cannot automatically determine which change to keep. I would inspect the conflicting section, choose or combine the correct changes, remove the conflict markers, then add and commit the resolved file.

**2.7** A user reports a bug that you **cannot reproduce** on your machine. Describe the steps you would take to investigate.

I would first ask the user what they are expecting for the result and what is produced instead. I will try to fix it by asking the version of the machine, and other details, and do the fixing accordingly.

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
[3, 2, 1]
b) Describe in one sentence what `f` does. Can you write it in one line?
f is the name of the function that reverse the order of contents inside the list
[lst[i] for i in range(len(lst) - 1, -1, -1)]

### 3.2 — Predict the output (Python)

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
```

a) What is printed on each line?
["a"]
["a", "b"]
b) Is this likely the intended behavior? If not, how would you fix it?
no, that is not the intended behaviour of the function, I would fix it by having None as the default content of "bucket" so it will not print the content before.
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
### 3.3 — Predict the output (JavaScript)

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

a) What is logged to the console?
3, 3, 3
b) Change **one word** so that it logs `0 1 2`. Explain why it works.
Change var to let.
let creates a separate block-scoped i for each iteration of the loop. Therefore, when each delayed function runs, it remembers its corresponding value: 0, 1, and 2.

### 3.4 — Find the bug

```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

a) Under what input does this function fail? What error occurs?
the function will fail if the input is string, the error is typeError
b) Rewrite the function to handle that case sensibly.

def average(nums):
    total = 0
    for n in nums:
        total += float(n)
    return total / len(nums)
### 3.5 — Write a SQL query

Given these tables:

```
employees(id, name, dept_id, salary)
departments(id, name)
```

Write a query that returns **each department's name and average salary**, but **only for departments with more than 3 employees**, sorted from **highest to lowest** average salary.

SELECT d.name, AVG(e.salary) AS average_salary
FROM departments d
JOIN employees e
    ON d.id = e.dept_id
GROUP BY d.id, d.name
HAVING COUNT(e.id) > 3
ORDER BY average_salary DESC;

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

def split_input (Input):
    split_input = Input.split()
    split_input = split_input[::-1]
    return " ".join(split_input)

### 4.2 — Balanced Brackets

Write a function that returns `true` if a string's brackets `()`, `[]`, `{}` are **balanced and correctly nested**, otherwise `false`. Other characters are ignored.

```
"(a[b]{c})"  -> true
"([)]"       -> false
"(("         -> false
""           -> true
```

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)

    return not stack
*Question: what is the time and space complexity of your solution?*

time: O(n)
space:O(n) 
### 4.3 — Top-N Word Frequency

Write a function `top_words(text, n)` that returns the `n` most frequent words in `text`.

- Case-insensitive (`"The"` and `"the"` are the same word)
- Ignore punctuation `. , ! ? ; :`
- If two words have the same count, sort them alphabetically

```
text = "The cat and the hat. The cat sat!"
top_words(text, 2)  ->  [("the", 3), ("cat", 2)]
```

def top_words(text, n):
    import re
    from collections import Counter

    # Normalize the text to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[.,!?;:]', '', text)

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the n most common words, sorted by count and then alphabetically
    most_common = word_counts.most_common()
    most_common.sort(key=lambda x: (-x[1], x[0]))

    return most_common[:n]
