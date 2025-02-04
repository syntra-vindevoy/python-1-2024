def chop(lst):
    del lst[0]
    del lst[-1]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]

    print(chop(lst))
    print(lst)
