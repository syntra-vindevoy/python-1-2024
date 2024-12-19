
my_list = ['a','b','d','c','e']

def swap_by_position(index_a,index_b):
    my_list.insert(index_a,my_list.pop(index_b))

def swap_by_index(index_a,index_b):
    my_list[index_a], my_list[index_b] = my_list[index_b], my_list[index_a]

def swap_by_value(char_1,char_2):
    index_1 = my_list.index(char_1)
    index_2 = my_list.index(char_2)
    my_list[index_1], my_list[index_2] = my_list[index_2], my_list[index_1]

print(my_list)

swap_by_position(3,2)
print(my_list)  

swap_by_index(2,3)
print(my_list)  

swap_by_value('a','e')
print(my_list)