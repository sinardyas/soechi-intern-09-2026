# Angad - Internship Assessment


## Part 1 — Multiple Choice (20 pts)

**1.1** What is the time complexity of **binary search** on a sorted array of `n` elements?
b) O(log n)


**1.2** Which data structure follows **Last In, First Out (LIFO)**?
b) Stack


**1.3** An HTTP response with status code **404** means:
c) Resource not found


**1.4** Which HTTP method is conventionally used to **create** a new resource in a REST API?
b) POST


**1.5** Which SQL statement removes **specific rows** matching a condition, while keeping the table?
b) `DELETE FROM ... WHERE ...`


**1.6** Which Git command **creates a new branch and switches to it**?
c) `git checkout -b feature`


**1.7** Which of the following is **NOT** one of the core principles of Object-Oriented Programming?
d) Compilation


**1.8** What is the main purpose of a **primary key** in a relational database table?
b) To uniquely identify each row


**1.9** What is the **average** time complexity of looking up a key in a hash map / dictionary?
c) O(1)

**1.10** Which of the following is **valid JSON**?
c) `{"name": "Budi", "age": 21}`

---

## Part 2 — Short Answer Theory (21 pts)

**2.1** What is the difference between a **process** and a **thread**?

A process is a program that is loaded into the memory and is executed, while a thread is a small instruction or step 
perfomed within the process to make it work. A key difference is that a process takes a much larger chunk of memory 
than threads, and usually if one process fails, another can still run after it. On the other hand, if one thread fails, 
the threads after that will also fail to do their task. For instance, a process may be opening a webpage on your browser, and the threads work to load the text with the right font and size, display the correct colours and etc..

**2.2** Compare **SQL (relational)** and **NoSQL** databases. Give one situation where you would choose each.

A SQL database is used when there is a fixed relationship between 2 or more entities/tables, such as many to one or one to one. While I am not very familiar with a NoSQL database, I do know that it is used when when there is a flexible storage or relationship of data between 2 or more entities/tables. For instance, when designing an online form for employees to fill in, if all 
boxes are required to be filled in a certain way, a SQL database can be used, however if the form allows employees to fill in various data of their choosing in any possible format, a NoSQL database would be optimal and would be able to deliver these results to you fast. 

**2.3** What is an **API**? What makes an API "RESTful"? Name at least two characteristics.

An API is an a application programming interface, when one interface communicates and transfers data between another interface, it ensures that the connected interface is the intended one, authenticating it. REST API is code that allows those 2 interfaces to properly communicate with each other, following a set of rules. 2 characteristics of this is that 
it is used in a client-server architecture, and the communication between these 2 endpoints is stateless.  

**2.4** Describe, at a high level, what happens when you type `https://www.example.com` into a browser and press Enter.

The browser first of all processes the URL and then tries to find out which server to use to be able to retrieve the information for the webpage. This is done using DNS as it converts the domain name into an IP address of the matching server. The browser will then establish a connection between the client and the server using TCP protocol and port address of the server. 
The browser then sends a HTTP GET request for the webpage to the server, to which the server replies by sending a HTML file using HTTP back to the browser. If all information needed is already present in the HTML file, the browser will display it on your screen

**2.5** Why do developers write **unit tests**? What makes a unit test "good"?

Unit tests help test a specific part of a program, like a function. These are considered good practice as they help developers find out whether the functions work as intended, when given a fixed set of inputs that test normal and edge cases, along with a set of expected outputs. 

**2.6** What is a **merge conflict** in Git, why does it happen, and how do you resolve one?

A merge conflict primarily happens if you make another branch from the main branch of the same file, and start coding on that branch, while someone else codes over the same part of the file on the main branch. When it comes time to merge and combine the code in second branch with the main branch, a merge conflict will arise since Git will be confused which version/code to keep and which one to remove. In order to resolve this, the developer has to manually decide which changes to keep or combine. 

**2.7** A user reports a bug that you **cannot reproduce** on your machine. Describe the steps you would take to investigate.

If the issue cannot be reproduced on my machine, it would be advisable to find out which device, operating system or dated software the user was using, and then try recreating the user conditions used all these details when the bug had occured. Moreover, if this is also unsuccessful, it could be most likely be an issue related to a third-party software or entitiy that interferes with my software that the user is using. In this case, it would be better to investigate on the possible interfering softwares and try and fix any integration issues or unauthorized actions. 

---

## Part 3 — Code Reading & Debugging (20 pts)

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
Output: [3,2,1]
b) Describe in one sentence what `f` does. Can you write it in one line? 
The function 'f' reverses the order of elements in a list. Writing it in one line would look like this: 
result = [items[i] for i in range (len(items) -1, -1, -1)]


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
No, the function likey wanted the letter passed into the function to be printed in a seperate list each time. A way to fix it would to be declare bucket as a list inside the function, not as a default argeument.  
def add_item(item):
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
It logs: 
3
3
3
b) Change **one word** so that it logs `0 1 2`. Explain why it works. 
We can change 'var' into 'let'. This is because 'let' creates a seperate block-scoped 'i' for each loop iteration, meaning every callback would remember it's own value. 



### 3.4 — Find the bug
```python
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
```

a) Under what input does this function fail? What error occurs? 
A TypeError may occur is a string is present in the list or iterable 'nums'. Or, if 'nums' is empty and the length is zero, a ZeroDivisionError may occur. 
b) Rewrite the function to handle that case sensibly.
def average(nums):
    if len(nums) > 0: 
        total = 0
        length = 0 
        for n in nums:
            if type(n) != str: 
                total += n
                length +=1
            else: 
                continue 
        return total / length 
    else: 
        return None 


### 3.5 — Write a SQL query
Given these tables:

```
employees(id, name, dept_id, salary)
departments(id, name)
```

Write a query that returns **each department's name and average salary**, but **only for departments with more than 3 employees**, sorted from **highest to lowest** average salary.

SELECT department.name, AVG(department.salary) as average_salary
FROM departments 
JOIN departments 
    ON departments.id = employees.dept_id
GROUP BY departments.id, departments.name 
HAVING COUNT(employees.id)> 3 
ORDER BY average_salary DESC

---




