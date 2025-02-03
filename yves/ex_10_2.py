def cumsum(lst: list[int]) -> list[int]:
    nl = []
    s = 0

    for i in lst:
        s += i
        nl.append(s)

    return nl

def cumsum2(lst: list[int]) -> list[int]:
    return [sum(lst[0:i+1]) for i in range(len(lst))]


if __name__ == '__main__':
    print(cumsum2([1, 2, 3, 4]))