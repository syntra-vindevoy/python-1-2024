# with open("words.txt") as f:
#     words = f.readlines()
#
# counter = 0
#
# def give_me_a_word():
#     global counter
#     word = words[counter]
#     counter += 1
#
#     return word.strip()
#
# print(give_me_a_word())
# print(give_me_a_word())


my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

my_list = [i for i in range(10)]

print(my_list)

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

my_dict = {chr(i + 97): i+1 for i in range(3)}
print(my_dict)