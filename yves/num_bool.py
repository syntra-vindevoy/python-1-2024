print(int(True))

if -1:
    print("yes")
    w = 1/0



def is_abecedarian(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False

    return True