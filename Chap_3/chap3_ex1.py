# def print_right(text):
#     text = text.strip() #(alle troep weg)
#     assert len(text) <= 40, "maximum length of text is 40 characters"
#     print(f"{(40 - len(text)) * ' '}{text}") #40 spaties en dan text
#
#
#
#
# def main():
#     #assert len(print_right("Tom")) == 40    #test of het idd 40 caracters is.
#     assert print_right("Jerry")[35:40] == "Jerry"    #test of de naam correct is
#     print_right("user's always wrong  ")
#
#
# if __name__ == "__main__":
#     main()

def print_right(text):
    text = text.strip()  # alle troep weg
    assert len(text) <= 40, "maximum length of text is 40 characters"
    formatted_text = f"{(40 - len(text)) * ' '}{text}"  # 40 spaties en dan text
    return formatted_text


def main():
    # assert len(print_right("Tom")) == 40    #test of het idd 40 caracters is.
    assert print_right("Jerry")[35:40] == "Jerry"  # test of de naam correct is
    print(print_right("user's always wrong  "))


if __name__ == "__main__":
    main()


