Here’s an example of an **HBO 5-level Python exam** covering lists, dictionaries, tuples, files, strings, and string sliding. Each section includes theoretical and practical questions to test understanding and application. 

---

## **Python Exam - HBO 5 Level**  
**Duration:** 2 hours  
**Total Marks:** 100  
**Instructions:** Answer all questions. Provide code solutions where required.

---

### **1. Lists (15 points)**

#### 1.1 Theory (5 points)  
- a) What is the difference between a list and a tuple in Python? Provide two key differences. (2 points)  
- b) Explain the concept of list slicing with an example. (3 points)

#### 1.2 Practical (10 points)  
- Write a function `find_even_numbers(lst)` that takes a list of integers as input and returns a new list containing only the even numbers.  

Example:  
```python
find_even_numbers([1, 2, 3, 4, 5, 6])  
# Output: [2, 4, 6]
```

---

### **2. Dictionaries (15 points)**

#### 2.1 Theory (5 points)  
- a) What is a dictionary in Python, and how is it different from a list? Provide an example to illustrate your explanation.  
- b) What happens if you try to access a key that does not exist in a dictionary? How can this issue be handled?

#### 2.2 Practical (10 points)  
- Write a function `count_words(sentence)` that takes a string as input and returns a dictionary where the keys are unique words and the values are the word counts. Ignore case.  

Example:  
```python
count_words("This is a test. This test is simple.")  
# Output: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}
```

---

### **3. Tuples (10 points)**

#### 3.1 Theory (4 points)  
- a) Why are tuples immutable? How does this benefit program execution?  
- b) Give an example where using a tuple is preferred over a list.

#### 3.2 Practical (6 points)  
- Write a function `tuple_operations(tpl)` that takes a tuple of integers and returns a new tuple with the following:  
  - The first element: the smallest number  
  - The second element: the largest number  
  - The third element: the sum of all numbers  

Example:  
```python
tuple_operations((5, 3, 9, 2, 8))  
# Output: (2, 9, 27)
```

---

### **4. File Handling (20 points)**

#### 4.1 Theory (8 points)  
- a) What are the key modes available for file operations in Python? Provide a brief description of each mode.  
- b) Explain the difference between `read()` and `readlines()`.

#### 4.2 Practical (12 points)  
- Write a Python script `write_and_read_file(filename, data)` that does the following:  
  1. Writes a list of strings (`data`) to a file, each on a new line.  
  2. Reads the content back from the file and returns it as a single string.  

Example:  
```python
data = ["Hello", "World", "Python is great"]  
write_and_read_file("example.txt", data)  
# Output: "Hello\nWorld\nPython is great\n"
```

---

### **5. Strings (25 points)**

#### 5.1 Theory (10 points)  
- a) What are f-strings in Python? Provide an example.  
- b) Explain the difference between `isalpha()`, `isdigit()`, and `isalnum()`. Provide an example for each.

#### 5.2 Practical (15 points)  
- Write a function `reverse_vowels(s)` that takes a string and returns 
it with only the vowels reversed while leaving other characters unchanged.  

Example:  
```python
reverse_vowels("hello world")  
# Output: "holle werld"
```

---

### **6. String Sliding (15 points)**

#### 6.1 Theory (5 points)  
- a) What is string sliding, and how can it be implemented using slicing?  
- b) Provide an example to explain how you can extract every third character from a string.

#### 6.2 Practical (10 points)  
- Write a function `find_substrings(s, k)` that takes a string `s` and an integer `k`
- and returns a list of all unique substrings of length `k` in `s`.  

Example:  
```python
find_substrings("abcabcbb", 3)  
# Output: ['abc', 'bca', 'cab', 'cbb']
```

---

### **Bonus Question (10 points)**  
Implement a program to solve the following problem:  
- Given a file containing a paragraph of text, find and print the top 3 most frequently occurring words. Ignore case and punctuation.  

---

Let me know if you'd like adjustments!