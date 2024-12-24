from functions import *
from icecream import ic


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