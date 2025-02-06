
def find_repeats(counter: dict) -> dict:
    for key in counter:
        if counter[key] == 1:
            del counter[key]

    return counter


def main():

    counter = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    print(find_repeats(counter))

if __name__ == "__main__":
    main()
