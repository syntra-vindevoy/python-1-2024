def read_words():
    try:
        with open("words.txt", 'r') as file:
            for line in file:
                # Split by whitespace to extract words
                for word in line.split():
                    yield word
    except FileNotFoundError:
        print(f"Error: The file 'words.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


for word in read_words():
    print(word)


def factorial_generator():
    """
    Generator function that yields successive factorials.

    Yields:
        int: The next factorial in the sequence.
    """
    result = 1
    n = 0
    while True:
        if n == 0 or n == 1:
            # 0! and 1! are both equal to 1
            result = 1
        else:
            # Multiply the current result with n to get n!
            result *= n
        yield result
        n += 1  # Move to the next number


# Example usage:
gen = factorial_generator()

# Generate the first 10 factorials
for i in range(10):
    print(f"Factorial of {i} is: {next(gen)}")