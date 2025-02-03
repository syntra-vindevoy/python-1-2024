def has_duplicates(lst: list):
    copy_lst = lst.copy()
    sorted_lst = sorted(copy_lst)

    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] == sorted_lst[i + 1]:
            print(sorted_lst[i])
            return True

    return False

