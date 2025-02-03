def has_reversed_pairs(words):
    repairs = []

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i] == words[j][::-1]:
                repairs.append(words[i])
                repairs.append(words[j])

    return repairs


with open("words.txt") as file:
    words = file.readlines()

    pairs = {}

    for word in words:
        word = word.strip()
        key = "".join(sorted(word))

        if key in pairs:
            pairs[key].append(word)
        else:
            pairs[key] = [word]

    for pair in pairs:
        if len(pair) > 1:
            repairs = has_reversed_pairs(pairs[pair])

            if len(repairs) > 1:
                print(repairs)

