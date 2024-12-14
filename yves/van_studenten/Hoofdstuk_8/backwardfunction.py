def reading_backwards():
    s = input("What string you want to read backwards?" )
    index = len(s) - 1
    while index > 0:
        print(s[index])
        index = index - 1

reading_backwards()