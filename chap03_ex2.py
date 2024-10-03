#Chapter 3 - Exercise 2
from six import print_


def print_right(text):
    text = text.strip()         #ommits spaces at the beginnen and the end of the string
    assert len(text) <= 40, "Max length of text is 40 char"

    #string_length = len(text)
    #space_length = 40 - string_length
    #print(" " * space_length + text)
    #print(f"{(40 - len(text)) * ' '}{text}")
    return f"{(40 - len(text)) * ' '}{text}"

def main():
    assert len(print_right("Hello World")) == 40
    assert print_right("Yves")[36:40] == "Yves"
    print(print_right("Pyyyyython"))
    print(print_right("   User's always abuse your system   "))
    #print_right("it's hard to type some text that's longer than a certain amount of characters without counting")

if __name__ == "__main__":
    main()