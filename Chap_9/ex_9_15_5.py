from datetime import datetime

# Open the file in read mode
def method_1():
    with open('words.txt', 'r') as f:
        # Read the content of the file
        content = f.read()
        words = content.replace("\n", "")
    # Count the characters
    return len(words)

def method_2():
    with open('words.txt', 'r') as f:
        content = f.read()
        return len(content) - content.count("\n")

if __name__ == "__main__":
    start = datetime.now()
    for _ in range(10000):
        character_count = method_1()
    end = datetime.now()
    print("Number of characters in the file:", character_count)
    print("Time taken for method_1:", end - start)

    start = datetime.now()
    for _ in range(10000):
        character_count = method_2()
    end = datetime.now()
    print("Number of characters in the file:", character_count)
    print("Time taken for method_2:", end - start)