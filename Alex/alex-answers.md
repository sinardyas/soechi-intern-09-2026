# Alex - Internship Assessment 

**Section 1**
-

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
- c) `git checkout -b feature`

**1.7** Which of the following is **NOT** one of the core principles of Object-Oriented Programming?
- d) Compilation

**1.8** What is the main purpose of a **primary key** in a relational database table?
- b) To uniquely identify each row

**1.9** What is the **average** time complexity of looking up a key in a hash map / dictionary?
- a) O(1)

**1.10** Which of the following is **valid JSON**?
- c) `{"name": "Budi", "age": 21}`

**Section 2**
- 

**2.1** What is the difference between a **process** and a **thread**?
- A process runs independently and has its own isolated memory space and resources, whilst many threads can be present inside a single process. Unlike processes, threads share the same memory space and run concurrently to perform multiple tasks within that process.

**2.2** Compare **SQL (relational)** and **NoSQL** databases. Give one situation where you would choose each.
- If data is structured and clear, I would choose an SQL (relational) database because SQL databases is strict and ensures data integrity. On the other hand, NoSQL provides a more flexible environment where unstructured or diverse data can be stored without it being very strict.

**2.3** What is an **API**? What makes an API "RESTful"? Name at least two characteristics.
- An API allows two different softwares to interact with eachtoher and share data with eachother. The API itself is a sort of list of rules where both softwares must follow to either send or receive eachother's data. An API being "RESTful" relies on it being a client-server based architecture where ideally all data is processed by the server and later sent to the client. An API being "RESTful" also means that it is stateless, as the server require that all requirements be fulfilled and that it doesn't store any context inbetween.

**2.4** Describe, at a high level, what happens when you type `https://www.example.com` into a browser and press Enter.
- The browser sends a message to the internet asking for the website. The server gets the message and sends back the HTML code so your computer can show the webpage.

**2.5** Why do developers write **unit tests**? What makes a unit test "good"?
- Developers write unit tests to ensure individual pieces of code, like a single function, work correctly on their own. A good unit test is one that tests specifically only one test.

**2.6** What is a **merge conflict** in Git, why does it happen, and how do you resolve one?
- Merge conflict happens when two people change the exact same line of code in different ways and try to combine their work, Git is then 'conflicted' on which one to keep. A manual review would need to be done to that code.

**2.7** A user reports a bug that you **cannot reproduce** on your machine. Describe the steps you would take to investigate.
- I would first find out what device this user in partiuclar was using and at what conditions it was used during the bug, if possible a crash log report would be highly informative. With this log, it would be possible to perhaps recreate the conditions much closely. If this is still not reproducable and the bug is isolated to that one person, it could be a false positive. Eitherway, it would be wise to fix whatever is possible with the knowledge from that log to prevent any future issues with any future machines.

**Section 3**
-

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
- [3, 2, 1]
b) Describe in one sentence what `f` does. Can you write it in one line?
- Function 'f' flips the order in a list, so in this case [1, 2, 3] becomes [3, 2, 1]. In a one liner we could do something like

```python
result = list(reversed(items))
```

### 3.2 — Predict the output (Python)

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
```

a) What is printed on each line?

```python
["a"]
["a", "b"]
```

b) Is this likely the intended behavior? If not, how would you fix it?
- The default list bucket=[] is created only once when the function is defined, so it keeps adding to the same list. The fix would be to make bucket a seperate statement inside the function.

```python
def add_item(item):
    bucket=[]
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
```

### 3.3 — Predict the output (JavaScript)

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

a) What is logged to the console?
- 3 3 3

b) Change **one word** so that it logs `0 1 2`. Explain why it works.
- the word var needs to be changed to let. Var's scope is global and i will always be 3, this effects callbacks and prints 3. Let fixes this as it is purely operates inside the blocks.

```javascript
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
// Output: 0, 1, 2
```

### 3.4 — Find the bug

```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

a) Under what input does this function fail? What error occurs?
- this could result in a division by 0 

b) Rewrite the function to handle that case sensibly.
- when len(nums) is 0 it simply returns a 0

```python
def average(nums):
	if len(nums) == 0:
		return 0

	total = 0

	for n in nums:
		total += n

	return total / len(nums)
```

### 3.5 — Write a SQL query

Given these tables:

```
employees(id, name, dept_id, salary)
departments(id, name)
```

```
SELECT
    d.name AS department_name,
    AVG(e.salary) AS average_salary
FROM departments AS d
JOIN employees AS e
    ON e.dept_id = d.id
GROUP BY d.id, d.name
HAVING COUNT(e.id) > 3
ORDER BY average_salary DESC;
```

**Section 4**
-

### 4.1 — Reverse the Words

Write a function that reverses the **order of words** in a sentence. Extra spaces between words should be collapsed into one, and leading/trailing spaces removed.

```
Input:  "  the ship   sails at dawn "
Output: "dawn at sails ship the"
```

```python
def f(text):
    reversed_text =" ".join(reversed(text.split()))
    return reversed_text

# Test Cases
print(f("  the ship   sails at dawn ")) # Expected: "dawn at sails ship the"
print(f("hello   world"))              # Expected: "world hello"
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

```python
def is_balanced(text):
	open_brackets = "([{"
	close_brackets = ")]}"
	matching_brackets = {
		")": "(",
		"]": "[",
		"}": "{"
	}
	stack = []

	for character in text:
		if character in open_brackets:
			stack.append(character)
		elif character in close_brackets:
			if not stack or stack.pop() != matching_brackets[character]:
				return False

	return len(stack) == 0

# Test Cases
print(is_balanced("(a[b]{c})")) # Expected: True
print(is_balanced("([)]"))      # Expected: False

# Complexity Answer:
# Time Complexity: O(n) because we iterate through the string once.
# Space Complexity: O(n) in the worst-case scenario (e.g., all open brackets "(((").
```

### 4.3 — Top-N Word Frequency

Write a function `top_words(text, n)` that returns the `n` most frequent words in `text`.

- Case-insensitive (`"The"` and `"the"` are the same word)
- Ignore punctuation `. , ! ? ; :`
- If two words have the same count, sort them alphabetically

```
text = "The cat and the hat. The cat sat!"
top_words(text, 2)  ->  [("the", 3), ("cat", 2)]
```
```python
def top_words(text, n):
	text = text.lower()

	for punctuation in ".,!?:;":
		text = text.replace(punctuation, " ")

	words = text.split()
	counts = {}

	for word in words:
		if word not in counts:
			counts[word] = 0
		counts[word] += 1

	sorted_words = sorted(counts, key=lambda word: (-counts[word], word))

	return [(word, counts[word]) for word in sorted_words[:n]]

# Test Cases
print(top_words("The cat and the hat. The cat sat!", 2)) 
# Expected: [('the', 3), ('cat', 2)]

print(top_words("Apple apple banana banana orange", 2)) 
# Expected: [('apple', 2), ('banana', 2)]
```



