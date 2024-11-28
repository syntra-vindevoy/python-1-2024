def total_length():
    with open("words.txt", "r") as f:
        words = f.read().split("\n")
        totaal = 0
        for word in words:
            lengte = len(word)
            totaal += lengte

    return totaal

print(total_length())

