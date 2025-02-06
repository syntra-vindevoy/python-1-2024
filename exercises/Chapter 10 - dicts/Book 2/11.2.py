# Exercise 11.2. Read the documentation of the dictionary method setdefault and use it
# to write a more concise version of invert_dict.

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


def main():
    d = {1: "a", 2: "b", 3: "c"}
    print(invert_dict(d))

if __name__ == '__main__':
    main()