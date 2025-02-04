def bisect_search(sorted_list, item):
    step = 0
    marker_low = 0
    marker_high = len(lst) - 1

    while True:
        step += 1
        marker_middle = (marker_low + marker_high) // 2
        item_middle = sorted_list[marker_middle]

        if item_middle == item:
            return True, step

        if item_middle > item:
            marker_high = marker_middle - 1
        else:
            marker_low = marker_middle + 1

        if marker_low == marker_high:
            return sorted_list[marker_low] == item, step


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(bisect_search(lst, 1))
    print(bisect_search(lst, 2))
    print(bisect_search(lst, 3))
    print(bisect_search(lst, 4))
    print(bisect_search(lst, 5))
    print(bisect_search(lst, 6))
    print(bisect_search(lst, 7))
    print(bisect_search(lst, 8))
    print(bisect_search(lst, 9))
    print(bisect_search(lst, 10))

    print(bisect_search(lst, 0))
    print(bisect_search(lst, 11))
