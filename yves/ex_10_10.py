def bisect_search(sorted_list, item, step = 1):
    if len(sorted_list) == 1:
        return item == sorted_list[0], step

    middle_index = len(sorted_list) // 2
    middle_item = sorted_list[middle_index]

    if middle_item == item:
        return True, step

    if middle_item > item:
        return bisect_search(sorted_list[:middle_index], item, step + 1)
    else:
        return bisect_search(sorted_list[middle_index+1:], item, step + 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(bisect_search(lst, 1))
    print(bisect_search(lst,2))
    print(bisect_search(lst,3))
    print(bisect_search(lst,4))
    print(bisect_search(lst,5))
    print(bisect_search(lst,6))
    print(bisect_search(lst,7))
    print(bisect_search(lst,8))
    print(bisect_search(lst,9))
    print(bisect_search(lst,10))

    print(bisect_search(lst, 0))
    print(bisect_search(lst, 11))
