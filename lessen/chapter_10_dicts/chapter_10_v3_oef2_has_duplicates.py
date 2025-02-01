"""
Write function called find_repeats that takes a dictionary that maps from each key to a counter, 
like the result from value_counts. 
It should loop through the dictionary and return a list of keys that have counts greater than 1. 
You can use the following outline to get started.

def find_repeats(counter):
    '''Makes a list of keys with values greater than 1.
    
    counter: dictionary that maps from keys to counts
    
    returns: list of keys
    '''
    return []

"""


def value_counts(word: str) -> dict[str:int]:
    counter = {}
    for char in word:
        counter[char] = counter.get(char, 0) + 1
    return counter


def find_repeats(counter):
    temp_list = list()
    for key, value in counter.items():
        if value > 1:
            temp_list.append(key)
    return temp_list


def example_1():
    banana_counter = value_counts("banana")
    repeats = find_repeats(banana_counter)


def example_2():
    counter1 = value_counts([1, 2, 3, 2, 1])
    repeats = find_repeats(counter1)
    repeats
    pass


if __name__ == "__main__":
    example_2()
