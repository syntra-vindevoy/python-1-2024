def main():

    #lists
    """
     - Write a Python program to:
     - Create a list of the first 10 multiples of 3.
     - Check if the number 15 is in the list.
     - Insert the number 7 at the second position of the list.
    """
    li= [x*3 for x in range(1,10)]
    print(li)
    print(f"{15 in li}")
    li.insert(1,7)
    print(li)

    #dict
    """
     - Write a program to create a dictionary from two lists:
     `keys = ['name', 'age', 'city']` and `values = ['Alice', 25, 'New York']`.
   - Given a dictionary: `person = {"name": "John", "age": 30}`, write a program to:
     - Check if the key `"age"` exists in the dictionary.
     - Print the value of the `"name"` key.
    """
    keys = ['name', 'age', 'city']
    values = ['Alice', 25, 'New York']
    dict_p= dict(zip(keys,values))
    print(dict_p)

    person = {"name": "John", "age": 30}
    t=person.get("age")
    print(f" value: {t}")
    t = person.get("lol")
    print(f" value: {t}")


    #strings
    """
     - Write a Python program to:
     - Remove all spaces from the string `"Python Programming is Fun"`.
     - Find the first occurrence of the letter `"o"` in `"hello world"`.
     - Convert the string `"12345"` into an integer.
    """
    s="Python Programming is Fun"
    print(s.replace(" ",""))
    print(s.find("o"))
    print(int("12345"))


    ### **File-Based Questions**
    """
    - Write a Python program to:
         - Create a text file named `data.txt` and write the following lines into it:
           ```
           Python is fun.
           Programming is creative.
           Learning is continuous.
           ```
         - Read and print the content of the file line by line.
    """
    with open("data.txt","w") as f:
        f.write("Python is fun.\nProgramming is creative.\nLearning is continuous.\n")
        f.close()

    with open("data.txt","r") as f:
        for line in f:
            print(line)

    ### **Integrating Files with Lists**
    """
    4. **Basic:**
       - Write a program to read a file `fruits.txt` containing names of fruits (one per line), and:
         - Append a new fruit name (e.g., `"Mango"`) to the file.
         - Read and print the updated content of the file.
    
    """
    with open("fruits.txt","a") as f:
        f.write("Mango\n")
        f.writelines(
            [
                "Apple\n",
                "Banana\n",
                "Cherry\n"
            ])
        f.close()
    with open("fruits.txt","r") as f:
        for line in f:
            print(line)


    ### **Integrating Files with Dictionaries**
    """
    - Create a file `employees.txt` containing data in the format:
         ```
         John, Developer
         Alice, Manager
         Bob, Analyst
         ```
         - Write a program to read the file and create a dictionary where the keys are names and the values are job titles.
         - Print the dictionary.
    """
    with open("employees.txt","r") as f:
        dict_employees=dict()
        for line in f:
            name,job=line.split(",")
            dict_employees[name]=job
    print(dict_employees)



    """
    ### **Integrating Files with Strings**
    10. **Basic:**
        - Write a program to read a file `paragraph.txt` and:
          - Count the number of characters in the file.
          - Count the number of sentences (assume sentences end with `.`).
          - Count the number of words.
    """

    count_char=0
    count_sent=0
    count_words=0
    with open("paragraph.txt","r") as f:
        for line in f:
            line=line.split(".")
            count_sent+=1
            for l in line:
                count_words+=len(l.split())
                count_char+=len(l)
    print(f"char: {count_char}\nsent: {count_sent}\nwords: {count_words}")

if __name__ == "__main__":
    main()