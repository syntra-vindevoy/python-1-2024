def main():
    #list
    """
     - Write a Python program that takes a list of integers and removes all duplicate values.
   - Given the list: `fruits = ["apple", "banana", "cherry", "banana", "apple"]`, write a program to:
     - Count the occurrence of each fruit.
     - Sort the list alphabetically.
    Returns:

    """
    doube_list = [1,2,3,4,1,5,6,7,8,9,10,7,8,9,10,11,12,13,74,15,16,16,17,18,19,20]
    print(doube_list)
    doube_list.sort()
    uniques=[]
    for i in range(len(doube_list)):
        if doube_list[i] not in doube_list[i+1:]:
            uniques.append(doube_list[i])
    print(uniques)

    fruits = ["apple", "banana", "cherry", "banana", "apple","cherry", "mango", "mango", "cherry"]
    print(fruits)
    fruits.sort()
    print(fruits)
    count_words = {}
    for i in range(len(fruits)):
        for j in range(i+1,len(fruits)):
          if fruits[i] == fruits[j]:
                count_words[fruits[i]] = count_words.get(fruits[i],0) + 1
    print(count_words)


    #dict
    """
     - Write a Python program to count the frequency of words in a sentence using a dictionary.
     For example: `"hello world hello"` → `{'hello': 2, 'world': 1}`.
   - Given the dictionary:
     `scores = {"Math": 88, "Science": 92, "English": 85}`, write a program to:
     - Print the subject with the lowest score.
     - Add a new subject `"History": 90`.
    """
    freq=dict()
    sentence="hello world hello".split()
    for word in sentence:
        freq[word]=freq.get(word,0)+1
    print(freq)

    scores = {"Math": 88, "Science": 92, "English": 85}
    print(scores)
    min_score=min(scores.values())
    for key,value in scores.items():
        if value==min_score:
            print(key)
    scores["History"]=90
    print(scores)




    #strings
    """
     - Write a Python program to:
         - Reverse the string `"Python"`.
         - Remove all vowels from the string `"Hello, World!"`.
         - Split the string `"apple,banana,cherry"` into a list of fruits.
    """
    print("Python".replace(" ","")[::-1])
    string_to_remove="Hello, World!"
    for i in string_to_remove:
        if i in "aeiouAEIOU":
            string_to_remove=string_to_remove.replace(i,"")
    print(string_to_remove)


    #file
    """
     - Write a Python program that reads a file `names.txt` containing one name per line (e.g., `"Alice\nBob\nCharlie"`) and:
         - Stores all names in a list.
         - Prints the total number of names.
         - Prints the names in alphabetical order.
    """
    with open("names.txt","r") as f:
        names=f.read().splitlines()
        print(names)
        print(len(names))
        names.sort()
        print(names)


    ### **Integrating Files with Lists**
    """
     - Write a program to read a file `scores.txt` containing student scores in the format:
         ```
         Alice, 85
         Bob, 78
         Charlie, 92
         ```
         - Store the data in a dictionary with names as keys and scores as values.
         - Print the name of the student with the highest score.
    """
    with open("scores.txt","r") as f:
        dict_scores=dict()
        for l in f.read().splitlines():
            name,score=l.split(",")
            dict_scores[name]=int(score)
        print(dict_scores)
        print(max(dict_scores.values()))

    """
     - Write a program to read a file `products.txt` containing product data in the format:
         ```
         ProductA, 100
         ProductB, 200
         ProductC, 150
         ```
         - Store the data in a dictionary with product names as keys and prices as values.
         - Calculate the total value of all products.
    """
    with open("products.txt","r") as f:
        dict_products=dict()
        for l in f.read().splitlines():
            name,price=l.split(",")
            dict_products[name]=int(price)
        print(dict_products)
        print(sum(dict_products.values()))




"""
11. **Intermediate:**
    - Write a Python program to search for a specific word in a file `document.txt` and:
      - Count how many times the word occurs.
      - Replace all occurrences of the word with another word and save the updated content to a new file `updated_document.txt`.

"""
def search_word(word,file):
    with open(file,"r") as f:
        count=0
        for l in f.read().splitlines():
            if word in l:
                count+=1
    return count

def replace_word(word,new_word,file, new_file):
    with open(file,"r") as f:
        content=f.read()
    with open(new_file,"w") as f2:
        f2.write(content.replace(word,new_word))




if __name__ == "__main__":
    main()
    print(search_word("Count","document.txt"))
    replace_word("Count","New Count","document.txt","updated_document.txt")

