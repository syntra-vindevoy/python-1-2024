def print_right (text):

    text=text.strip()
    assert len(text) <= 40, "Maximum length of text is 40 characters."

    return f"{(40 - len(text)) * ' '}{text}"

def main():
    print(print_right("Chiel"))
    print_right("Python")
    print_right("user's always abuse your system   ")
    #print_right("bla  bla                              bla bla               bla bla")

    assert len(print_right("chiel")) == 40 #controle lengte text tov 40 characters
    assert print_right("chiel") [35:40] == "chiel"

if __name__ == "__main__":
    main()