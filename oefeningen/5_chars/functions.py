
from itertools import combinations
from os import path
from pprint import pprint
from time import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Time taken to execute {func.__name__}:{end_time - start_time:.4f} seconds")
        return result
    return wrapper

def loop_function(function,amount,depth):
    for i in range(amount):
        function()

@timing
def get_5_char_combination_set(character_stringlist):
    character_combinations = set()
    length = len(character_stringlist)
    

    for i in range(0,length-4):
        char_1 = character_stringlist[i]
        for j in range (i+1,length-3):
            char_2 = character_stringlist[j]
            for k in range (j+1,length-2):
                char_3 = character_stringlist[k]
                for l in range (k+1,length-1):
                    char_4 = character_stringlist[l]
                    for m in range (l+1,length):
                        char_5 = character_stringlist[m]
                        character_combinations \
                        .add(''.join([char_1,char_2,char_3,char_4,char_5]))
    return character_combinations   



def get_wordlist_from_file(file_name: str):
    script_dir = path.dirname(__file__)

    file_path = path.join(script_dir, file_name)
    with open(file_path, "r") as f:
        words = f.read().split("\n")
    return words



def add_to_combination_dict(
        char:str,
        word_set:set[str],
        combination_dict:dict[str:set(str)]) \
            -> dict[str,set[str]]:
    
    this_word_set = set(word for word in word_set if char in word)
    combination_dict[char].add(this_word_set) 
    return combination_dict
