with open("../../Chapter 10 - dicts/Book 3/words.txt", "r") as f:
    words = f.read().split("\n") #kan ook splitlines() voor gebruiken ipv split("\n")

def lengthsum(words):

    length = 0

    for i in words:
        length += (len(i))

    return length

with open("../../Chapter 10 - dicts/Book 3/words.txt", "r") as f:
    words = f.read()

    words = words.replace("\n", "")
    print(len(words))

with open("../../Chapter 10 - dicts/Book 3/words.txt", "r") as f:
    words = f.read()

    print(len(words) - words.count("\n"))



def main():
    print(lengthsum(words))


if __name__ == '__main__':
    main()