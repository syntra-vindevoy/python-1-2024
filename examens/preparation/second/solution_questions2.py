from collections import Counter


def even_numbers(list_of_numbers: list[int]):
    return [x for x in list_of_numbers if x%2 == 0]

assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def count_words(text: str)-> dict[str, int]:
    list_words = text.lower().replace(".","").split()
    ret_dict:dict[str, int] = dict()
    for word in list_words:
        if word in ret_dict:
            ret_dict[word] += 1
        else:
            ret_dict[word] = 1
    return ret_dict

def count_words_2(text: str)-> dict[str, int]:
    list_words = text.lower().replace(".","").split()
    ret_dict:dict[str, int] = dict()
    for word in list_words:
        ret_dict[word] =  ret_dict.get(word, 0) + 1
    return ret_dict

def count_words_3(text: str) -> dict[str, int]:
    list_words = text.lower().replace(".", "").split()
    return {word: list_words.count(word) for word in set(list_words)}

def count_words_counter(text: str) -> dict[str, int]:
    return Counter(text.lower().replace(".", "").split())


assert count_words("This is a test. This test is simple.") == {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}
assert count_words_2("This is a test. This test is simple.") == {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}
assert count_words_3("This is a test. This test is simple.") == {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}
assert count_words_counter("This is a test. This test is simple.") == {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'simple': 1}

def tuple_operations(tpl)->tuple:
   return min(tpl),max(tpl),sum(tpl)

assert tuple_operations((5, 3, 9, 2, 8)) == (2, 9, 27)


def write_and_read_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")
    data_read = []
    with open(filename, "r") as file:
        for line in file:
            data_read.append(line.strip())
    return data_read

assert write_and_read_file("example.txt", ["Hello", "World", "Python is great"]) == ["Hello", "World", "Python is great"]


def reverse_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    s_list = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s_list[i] not in vowels:
            i += 1
            continue
        if s_list[j] not in vowels:
            j -= 1
            continue
        s_list[i], s_list[j] = s_list[j], s_list[i]
        i += 1
        j -= 1

    # Return the modified string
    return ''.join(s_list)

assert reverse_vowels("Hello World") == "Hollo Werld"


def find_substrings(s, k):
    return [s[x:x+k] for x in range(len(s)-(k-1))]

assert find_substrings("abcabcbb", 3)  == ['abc', 'bca', 'cab', 'abc', 'bcb', 'cbb']

def top_3_most_frequently_occurring_words():
    cache_dict = {}
    with open("superman_vs_bart_de_wever.txt", "r") as file:
        text = file.read().replace(".", "").lower().split()
        cache_dict=Counter(text)
    return sorted(cache_dict.items(), key=lambda x: x[1], reverse=True)[:3]



if __name__ == '__main__':
    print(even_numbers([1, 2, 3, 4, 5, 6]))
    print(count_words("This is a test. This test is simple."))
    print(tuple_operations((5, 3, 9, 2, 8)))
    data = ["Hello", "World", "Python is great"]
    write_and_read_file("example.txt", data)
    print(reverse_vowels("Hello World"))
    print(find_substrings("abcabcbb", 3))
    print(top_3_most_frequently_occurring_words())