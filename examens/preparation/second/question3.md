Here's a **combined exercise** that integrates **lists**, **dictionaries**, **tuples**, **file handling**, **strings**, and **string sliding** into a single problem. 

---

## Combined Exercise: Text Analysis System  
**Total Marks:** 30  
**Scenario:**  
You are tasked with building a **Text Analysis System** that processes a paragraph of text from a file and performs the following operations:  

### **Requirements:**

1. **Read Input from a File (5 points)**  
   Write a function `read_text_file(filename)` that reads a file containing a paragraph of text and returns the content as a string.  

2. **Word Count and Frequency Analysis (10 points)**  
   Write a function `analyze_text(text)` that takes a string input and returns:  
   - A **dictionary** where keys are unique words (ignoring case) and values are their frequencies.  
   - A **tuple** containing:
     - The most frequently occurring word(s).  
     - The total number of unique words.  

   Example:  
   ```python
   text = "Python is great. Python is easy to learn. Learn Python!"
   analyze_text(text)
   # Output: 
   # (
   #   {'python': 3, 'is': 2, 'great': 1, 'easy': 1, 'to': 1, 'learn': 2},
   #   ('python', 6)
   # )
   ```

3. **Extract Substrings (Sliding Window) (5 points)**  
   Write a function `find_unique_substrings(word, k)` that takes a **single word** and an integer `k`, and returns a **list** of all unique substrings of length `k` in that word.  

   Example:  
   ```python
   find_unique_substrings("hello", 3)  
   # Output: ['hel', 'ell', 'llo']
   ```

4. **Write Results to a File (5 points)**  
   Write a function `write_analysis_to_file(filename, analysis_data)` that takes:  
   - A filename to write the results to.  
   - The output of `analyze_text()` (dictionary and tuple).  
   Write the word frequencies and most frequent word(s) to the file in a readable format.  

5. **Full Pipeline (5 points)**  
   Combine the above functions to:  
   - Read the input from a file (`input.txt`).  
   - Analyze the text using `analyze_text()`.  
   - Extract all unique substrings of length 3 from the most frequent word(s).  
   - Write the analysis and substrings to `output.txt`.  

---

### **Expected Workflow Example:**

Given the input file `input.txt` with the following content:  
```
Python is powerful. Python is flexible. Python is loved by many!
```

The pipeline would:  
1. Read the text from `input.txt`.  
2. Analyze the text:  
   ```python
   # Word Frequencies: {'python': 3, 'is': 3, 'powerful': 1, 'flexible': 1, 'loved': 1, 'by': 1, 'many': 1}
   # Most Frequent Word(s): 'python', 'is' (both with frequency 3)
   ```
3. Extract substrings of length 3 from the word "python":  
   ```python
   ['pyt', 'yth', 'tho', 'hon']
   ```
4. Write the results to `output.txt`:  
   ```
   Word Frequencies:
   python: 3
   is: 3
   powerful: 1
   flexible: 1
   loved: 1
   by: 1
   many: 1

   Most Frequent Word(s): python, is (3 occurrences)

   Unique Substrings of 'python' (length 3):
   ['pyt', 'yth', 'tho', 'hon']
   ```

---

Would you like the solution code for this exercise?