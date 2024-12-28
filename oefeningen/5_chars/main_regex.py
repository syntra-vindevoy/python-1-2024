
from functions import *
import re

@timing
def main_1():

    def matching_words(text, regex_pattern):
        matches = re.findall(r'\b' + regex_pattern + r'\b', text, re.IGNORECASE)
        return len(matches)

    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, "words.txt")
    with open(file_path, "r") as f:
        text = f.read()
    char_list = string.ascii_lowercase
    combinations = get_char_combination_set(char_list, 5)
    for comb in combinations:
        comb = "abcd"
        regex_pattern = r"\w*[" + comb + r"]\w*"
        matchings = matching_words(text, regex_pattern)
        #ic(matchings)     



if __name__ == "__main__":
    main_1()

