with open("words.txt") as file:
    words = file.readlines()

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i].strip() == words[j].strip()[::-1]:
                print(words[i].strip(), words[j].strip())
