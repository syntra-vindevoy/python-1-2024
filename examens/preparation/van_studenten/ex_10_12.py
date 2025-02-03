def interlock(str1, str2):
    zipped = zip(str1, str2, strict=False)

    interlocked = "".join(["".join(z) for z in zipped])

    if len(str1) != len(str2):
        if len(str1) > len(str2):
            interlocked += str1[len(str2):]
        else:
            interlocked += str2[len(str1):]


if __name__ == '__main__':
    interlock("abc", "defghi")
