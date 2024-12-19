import string

def five_chars():
    combinations = []

    for l_1 in string.ascii_lowercase[:22]:
        for l_2 in string.ascii_lowercase[1:23]:
            for l_3 in string.ascii_lowercase[2:24]:
                for l_4 in string.ascii_lowercase[3:25]:
                    for l_5 in string.ascii_lowercase[4:26]:
                        combinations.append(l_1 + l_2 + l_3 + l_4 + l_5)

    print(len(combinations))

    with open("words.txt", "r") as file:
        words = file.read().splitlines()

        print("number of words:", len(words))
        return
        min_found = len(combinations)
        combo = []

        for combination in combinations:
            for word in words:
                count_words = 0
             found = false

            for letter in combination:
                if letter in word:
                    found = True

            if not found:
                count_words += 1

        if count_words < min_found:
            min_found = count_words
            combo = combination

        print(combinations)