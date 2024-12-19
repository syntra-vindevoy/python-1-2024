
from pprint import pprint

numbers = range(1, 10)
number_list = list(numbers)
pprint(list(number_list))  # [1, 2, 3, 4, 5]


reverse = slice(None,None,-1)
first_five = slice(5)

pprint(number_list[reverse])  # [5, 4, 3, 2, 1]
pprint(number_list[first_five])  # [1, 2, 3, 4, 5]