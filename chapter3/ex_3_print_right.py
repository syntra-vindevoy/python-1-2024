def print_right(text):
    text = text.strip()

    assert len(text) <= 40, "Maximum length of text is 40 characters"

    return f"{(40 - len(text)) * ' '}{text}"

def main():
    assert len(print_right("Yves")) == 40
    assert print_right("Yves")[36:40] == "Yves"
    print(print_right("Python"))
    print(print_right("User's always abuse your system  "))
    # print_right("  in the most unusual ways, you never even dreamt of.  Really, they drive me mad.")

if __name__ == '__main__':
    main()
