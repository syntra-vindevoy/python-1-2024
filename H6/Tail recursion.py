# tail recursion is recursion waarbij je de tussenwaarden bijhoudt

def fact(n: int, t: int = 1) -> int:
    if n < 2
        return 1

    return n * fact(n - 1, n * t)

assert fact(0) == 1
assert fact(1) == 1
assert fact(2) == 2
assert fact(3) == 6
assert fact(4) == 24
assert fact(5) == 120
assert fact(6) == 720

#Hiermee kan je oneindig grote faculteiten berekenen, je heeft iedere keer 2 waarden mee waaronder u tussenresultaat
#Hierdoor kan je recursie gebruiken zonder met de stack in problemen te komen

