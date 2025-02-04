
def main():
    """
   - Write a Python function that rotates a list by `n` positions. For example:
     - Input: `lst = [1, 2, 3, 4, 5], n = 2`
     - Output: `[4, 5, 1, 2, 3]` (if rotated to the right).
   - Write a program that splits a list into two halves and swaps them. For example:
     - Input: `[1, 2, 3, 4, 5, 6]`
     - Output: `[4, 5, 6, 1, 2, 3]`
    """
    #list
    lst = [1, 2, 3, 4, 5]
    print(lst)
    n=2
    lst = lst[n+1:]+lst[:n+1]
    print(lst)

    lst = [1, 2, 3, 4, 5, 6]
    print(lst)
    middle=len(lst)//2
    lis1=lst[:middle]
    lis2=lst[middle:]

    lst=lis2+lis1
    print(lst)

#dict
"""
- Write a Python function that takes a dictionary where keys are strings and values are lists, and returns a dictionary with the same keys but sorted lists as values.
 Example input: `{"a": [3, 1, 2], "b": [5, 4]} → {"a": [1, 2, 3], "b": [4, 5]}`.
- Write a program that finds the intersection of two dictionaries.
 For example:
 - Dict1: `{"a": 1, "b": 2, "c": 3}`
 - Dict2: `{"b": 2, "c": 4, "d": 5}`
 - Output: `{"b": 2}`.
"""
def sort_dict(dict1)->dict:
    for key,value in dict1.items():
        dict1[key]=sorted(value)
    return dict1

def intersection(dict1,dict2)->dict:
    ret=dict()
    for key,value in dict1.items():
        if key in dict2:
            ret[key]=value
    return ret


#strings
"""
  - Write a Python function that checks if two strings are anagrams (contain the same characters in the same frequency).
     Example: `"listen"` and `"silent"` → True.
   - Write a program that extracts all the digits from a string. For example:
     Input: `"abc123xyz456"` → Output: `[1, 2, 3, 4, 5, 6]`.
"""
def is_anagram(string1,string2):
    return sorted(string1)==sorted(string2)

def extract_digits(string):
    return string.replace(" ","").split()

print(extract_digits("abc123xyz456"))


#files
"""
 - Write a Python program that reads a file `numbers.txt` containing integers (one per line) and:
     - Stores the integers in a list.
     - Calculates and prints the sum of all numbers.
     - Finds and prints the largest and smallest numbers.
"""
def files():
    with open("numbers.txt","r") as f:
        numbers=[int(i) for i in f.read().splitlines()]
        print(numbers)
        sum=0
        for i in numbers:
            sum+=int(i)
        print(sum)
        print(min(numbers))
        print(max(numbers))


### **Integrating Files with Lists**

"""
- Write a Python program that reads a file `sentences.txt` containing multiple sentences and:
     - Splits each sentence into words and stores them in a list.
     - Counts the total number of words.
     - Finds the longest word in the file.
"""
with open("sentences.txt","r") as f:
    for line in f:
        line=line.replace("."," ").replace("!"," ").replace("?"," ").lower()
        lined=line.split()
        if len(lined)!=0:
            print(lined)
            print(len(lined))
            print(max(lined,key=len))


"""
 - Write a program to merge two files, `file1.txt` and `file2.txt`, containing dictionaries stored in JSON-like format. Example:
     ```
     file1.txt: {"a": 1, "b": 2}
     file2.txt: {"b": 3, "c": 4}
     ```
     - Merge the dictionaries and handle overlapping keys by summing their values. Save the result to a new file `merged.txt`.

"""
import json
with open("file1.txt","r") as f:
    with open("file2.txt","r") as f2:
        dict1:dict = json.load(f)
        dict2:dict = json.load(f2)
        for key,value in dict1.items():
            if  key in dict2:
                dict1[key]=dict1[key]+dict2[key]
                dict2.pop(key)
        for key, value in dict2.items():
                dict1[key] = dict2[key] + dict1.get(key, 0)
        with open("merged.txt","w") as f3:
            f3.write(str(dict1))




"""
12. **Advanced:**
    - Write a Python program that reads a file `log.txt` containing log entries in the format:
      ```
      2025-01-01 INFO Starting application
      2025-01-01 ERROR Failed to connect
      2025-01-02 INFO Process completed
      ```
      - Extract and count the number of log entries for each level (`INFO`, `ERROR`, etc.).
      - Save the counts to a file `log_summary.txt`.

"""

def log_summary():
    levels=["INFO","ERROR","WARN","DEBUG"]
    with open("log.txt","r") as f:
        dict_log=dict()
        for line in f:
            for level in levels:
                if level in line:
                    dict_log[level]=dict_log.get(level,0)+1
        with open("log_summary.txt","w") as f2:
            f2.write(str(dict_log))



if __name__ == "__main__":
    main()
    print(intersection({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5}))
    print(sort_dict({"a": [3, 1, 2], "b": [5, 4]}))
    print(extract_digits("abc123xyz456"))
    print(is_anagram("listen","silent"))
    files()
    log_summary()