def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True

def is_sorted2(lst):
    return all([lst[i] <= lst[i + 1] for i in range(len(lst) - 1)])



if __name__ == '__main__':
    print(is_sorted([1, 2, 3, 4]))
    print(is_sorted2([1, 2, 3, 0]))
