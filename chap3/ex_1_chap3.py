def print_right(text):
    return(f"{(40 - len(text)) * ' '}{text}")

def main():
    print_right("Yves")
    print_right("Python")
    print_right("User's always abuse your system")

if __name__== '__main__':
    main()