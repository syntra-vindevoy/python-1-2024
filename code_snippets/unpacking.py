numbers = [1, 2, 3, 4, 5]
num_1, num_2, num_3, num_4, num_5 = numbers
print(num_1, num_2, num_3, num_4, num_5)  # 1 2 3 4 5

numbers = [1, 2, 3, 4, 5]
num_1, *num_2, num_3 = numbers
print(num_1, num_2, num_3)  # 1 [2, 3, 4] 5


