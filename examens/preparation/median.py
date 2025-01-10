def main():
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

if __name__ == "__main__":
    main()

