import time

def read_words_append(filename):
    """
    Reads a file and builds a list using the append method.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list containing one word per element.
    """
    words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            words.append(word)
    return words

def read_words_concat(filename):
    """
    Reads a file and builds a list using t = t + [x].

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list containing one word per element.
    """
    words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            words = words + [word]
    return words

def measure_time(func, filename):
    """
    Measures the execution time of a function.

    Args:
        func (callable): The function to measure.
        filename (str): The filename to pass to the function.

    Returns:
        float: The time taken by the function in seconds.
    """
    start_time = time.time()
    func(filename)
    end_time = time.time()
    return end_time - start_time

# Example usage:
filename = "words.txt"  # Ensure 'words.txt' is in the same directory

# Measure time for each function
append_time = measure_time(read_words_append, filename)
concat_time = measure_time(read_words_concat, filename)

print(f"Time using append: {append_time:.6f} seconds")
print(f"Time using concatenation: {concat_time:.6f} seconds")
