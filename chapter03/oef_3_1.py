def print_right(text, length):
    text = text.strip() #gooit alle spaties eruit van voor en vanachter
    length_string = len(text)
    leading_spaces = (length - length_string) * " "

    assert len(text) <= 40, "maximum length of text is 40 characters"

    return f"{leading_spaces}{text}"

def main():
    print(print_right("test", 40))
    assert len(print_right("test", 40)) == 40
    assert print_right("test", 40)[36:40] == "test"  #Dit is een test, de string start bij positie 0 tot 39. Dus kan je het laatste ook testen. 36:40 test dus positie 36 tot 39
    print(print_right("Python", 40))
    print(print_right("user's always abuse your system  ", 40))

if __name__ == "__main__":
    main()







#asserts bijschrijven
#de print uit uw functie halen, en gewoon retourneren.
#vb: assert factorial(0) == 1