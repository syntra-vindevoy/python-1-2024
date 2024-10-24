def for_with_string(text: str):
    for i in text:
        print(i, end=" ")
    print()  # finishing on new line


def name_lower(text: str):
    text.lower()


def main():
    for_with_string("Hello")


if __name__ == "__main__":
    main()
