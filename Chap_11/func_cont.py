from Chap_11.Extra_ex2 import change_salary
from Chap_11.extra_ex1 import combine_nested_lists

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print(change_salary(sample_dict, 'Brad', 8500))

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
print(combine_nested_lists(list1, list2))