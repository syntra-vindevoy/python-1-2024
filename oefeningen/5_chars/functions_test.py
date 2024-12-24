from functions import *
from icecream import ic

ic.disable()

assert char_in_word('a','abc') == True
assert char_in_word('z','abc') == False


assert char_not_in_word('a','abc') == False
assert char_not_in_word('z','abc') == True


assert char_in_words('a',{'abc','efg'}) == {'abc'}
assert char_not_in_words('a',{'abc','efg'}) == {'efg'}


assert any_char_in_word(['a','b','c'],'abc') == True
assert any_char_in_word(['z','y','x'],'abc') == False
assert any_char_in_word(['a','y','x'],'abc') == True


assert no_char_in_word(['z','y','x'],'abc') == True
assert no_char_in_word(['z','y','x'],'xyz') == False
assert no_char_in_word(['a','y','x'],'abc') == False


assert any_char_in_words(['a','b','c'],{'abc','efg'}) == {'abc'}
assert any_char_in_words(['z','y','x'],{'abc','efg'}) == set()
assert any_char_in_words(['a','y','x'],{'abc','efg'}) == {'abc'}


assert no_char_in_words(['z','y','x'],{'abc','efg'}) == {'abc','efg'}
assert no_char_in_words(['z','y','x'],{'xyz','efg'}) == {'efg'}
assert no_char_in_words(['a','y','x'],{'abc','efg'}) == {'efg'}


assert word_to_set('abc') == {'a','b','c'}
assert word_to_set('xyz') == {'x','y','z'}


assert get_char_combination_set(['a', 'b', 'c', 'd', 'e'], 5) == {'abcde'}
assert get_char_combination_set(['a', 'b', 'c', 'd', 'e'], 4) == {'abcd', 'abce', 'abde', 'acde', 'bcde'}
assert get_char_combination_set(['a', 'b', 'c', 'd', 'e'], 3) == {'abc', 'abd', 'abe', 'acd', 'ace', 'ade', 'bcd', 'bce', 'bde', 'cde'}
assert get_char_combination_set(['a', 'b', 'c'], 2) == {'ab','ac','bc'}


assert  get_char_combination_set(string.ascii_lowercase, 5) == \
        get_5_char_combination_set(string.ascii_lowercase)

def easy_case():
    word_list = {"auto",'bus','step','abba'}
    chars = 'abc'
    char_combinations = get_char_combination_set(chars,2) 
    assert char_combinations == {'ab','ac','bc'}

    comb_with_char_dict         =   {}
    comb_without_char_dict      =   {}
    words_with_char_dict        =   {}
    words_without_char_dict     =   {}

    ic.enable()
    adding_dict = {comb: 0 for comb in char_combinations}
    ic(adding_dict)

    word_list_length = len(word_list)
    subtracting_dict = {comb: word_list_length for comb in char_combinations}
    ic(subtracting_dict)
    ic.disable()

    for char in chars:
        ic(char)
        
        comb_with_char      =   char_in_words(char,char_combinations)
        comb_without_char   =   char_not_in_words(char,char_combinations)
        words_with_char     =   char_in_words(char,word_list)        
        words_without_char  =   char_not_in_words(char,word_list)

        ic(comb_with_char)
        ic(comb_without_char)
        ic(words_with_char)
        ic(words_without_char)


        '''
        comb_with_char_dict     +=   char_count(chars,comb_with_char)
        comb_without_char_dict  +=   char_count(chars,comb_without_char)
        words_with_char_dict    +=   char_count(chars,words_with_char)
        words_without_char_dict +=   char_count(chars,words_without_char)
        '''
        



ic.disable()       

easy_case()
    

