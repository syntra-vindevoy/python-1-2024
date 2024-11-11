def has_duplicates(t):
    s = set(t)
    return len(s) < len(t)


def main():
    s1 = set()
    s1.add(1)
    s1.add(2)
    s1.add(3)
    for i in s1:
        print(i)

    s2 = set('acd')
    for i in s2:
        print(i, end=" ")

    s3 = s1.union(s2)
    print(s3)

    print(set("word_counter") - set("word_list"))

    print(set('ab') <= set('abc'))


if __name__ == '__main__':
    main()
