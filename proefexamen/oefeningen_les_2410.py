def count_to_n(number):
    x = 1
    for i in range(2, number+1):
        x = x + i
    return x

print(count_to_n(100))