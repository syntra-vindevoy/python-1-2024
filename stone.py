# 1, 3, 9, 27 = 40
# -1, -3, -9, -27 = -40


def get_solution_list():
    """
    geeft alle mogelijke combinaties van 1, 3, 9 en 27
    """
    total_set = set()
    for i in [1, 0, -1]:
        for j in [3, 0, -3]:
            for k in [9, 0, -9]:
                for l in [27, 0, -27]:
                    total = i + j + k + l
                    if total > 0:
                        total_set.add(total)
    return total_set


def get_solution_version1(n):
    """
    Probeert alle combinaties tot de som bereikt is.
    Alle items voorbij de som worden genegeerd.
    """
    for l in [27, 0]:
        for k in [-9, 0, 9]:
            for j in [-3, 0, 3]:
                for i in [-1, 0, 1]:
                    if l + k + j + i == n:
                        return l, k, j, i
    return None


def get_solution_version2(n):
    """
    functie kijkt eerst of de 27-steen gebruikt wordt, positief of negatief.
    De range om de 27-steen te gebruiken is 27 - 9 - 3 - 1 <= n <= 27 + 9 + 3 + 1
    Als de 27 steen gebruikt wordt, wordt dit bijgehouden en wordt de waarde in min (of meer) gebracht.

    Zelfde principe wordt toegepast voor de 9 steen: steen gebruiken of niet?
    waarde in min of meer brengen. enzovoort.

    """
    stone_27 = 0
    stone_9 = 0
    stone_3 = 0
    stone_1 = 0

    # using stone 27?
    if +27 - 9 - 3 - 1 <= n <= +27 + 9 + 3 + 1:
        stone_27 = +27
        n -= stone_27

    # using stone 9?
    if +9 - 3 - 1 <= n <= +9 + 3 + 1:
        stone_9 = +9
    elif -9 - 3 - 1 <= n <= -9 + 3 + 1:
        stone_9 = -9

    n -= stone_9

    # using stone 3?
    if -3 - 1 <= n <= -3 + 1:
        stone_3 = -3
    elif +3 - 1 <= n <= +3 + 1:
        stone_3 = +3

    n -= stone_3

    # using stone 1?
    stone_1 = n

    return stone_27, stone_9, stone_3, stone_1


def get_solution_version3(n):
    """
    cleanere weergave (minder leesbaar, duidelijk)
    """

    stone_27 = 0
    stone_9 = 0
    stone_3 = 0
    stone_1 = 0

    # using stone 27?
    if 14 <= n <= 40:
        stone_27 = +27
        n -= stone_27

    # using stone 9?
    if 5 <= n <= 13:
        stone_9 = +9
    elif -13 <= n <= -5:
        stone_9 = -9

    n -= stone_9

    # using stone 3?
    if -4 <= n <= -2:
        stone_3 = -3
    elif +2 <= n <= +4:
        stone_3 = +3

    n -= stone_3

    # using stone 1?
    stone_1 = n

    return stone_27, stone_9, stone_3, stone_1


def get_solution_version5(n):
    """
    gebruik van trinair talstelsel
    """
    if n == 0:
        return "0"
    trinary = ""
    while n != 0:
        remainder = n % 3
        n = n // 3
        if remainder == 2:
            remainder = -1
            n += 1
        trinary = str(remainder) + trinary
    return trinary


def get_solution_version6(n):
    """ 
    trinair met while loop en list ipv string
    """
    if n == 0:
        return [0]
    trinary = []
    while n != 0:
        remainder = n % 3
        n = n // 3
        if remainder == 2:
            remainder = -1
            n += 1
        trinary.insert(0, remainder)
    return trinary



def get_solution_version7(n):
    """
    voor duidelijkere weergaven van de gewichten 
    """
    power = -1
    if n == 0:
        return [0]
    trinary = []
    while n != 0:
        power += 1
        remainder = n % 3
        n = n // 3
        if remainder == 2:
            remainder = -1
            n += 1
        trinary.insert(0, remainder * 3 ** (power))
    return trinary

# met trinair stelsel en tail recursion
def get_solution_version8(n):
    def helper(n, power, trinary):
        if n == 0:
            return trinary
        remainder = n % 3
        n = n // 3
        if remainder == 2:
            remainder = -1
            n += 1
        trinary.insert(0, remainder)
        trinary.insert(0, remainder * 3**power)
        return helper(n, power + 1, trinary)

    return helper(n, 0, [])



# 27, 9, 3, 1 werd verwijderd om rekentijd niet te beinvloeden.
def get_solution_version9(n):
    def helper(n, trinary):
        if n == 0:
            return trinary
        remainder = n % 3
        n = n // 3
        if remainder == 2:
            remainder = -1
            n += 1
        trinary.insert(0, remainder)
        return helper(n, trinary)

    return helper(n, [])


def main():
    for i in range(1, 41):
        print(i, get_solution_version9(i))

    print(500, get_solution_version9(500))
    print(1000, get_solution_version9(1000))


if __name__ == "__main__":
    main()

# test
