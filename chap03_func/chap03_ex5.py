#Chapter 3 - Exercise 5

def bottle_verse(n):
    assert n > 0, "n must be greater than zero"
    print(f"{n} bottles of beer on the wall")
    print(f"{n} bottles of beer")
    print(f" Take one down, pass it around")
    print(f"{n - 1} bottles of beer on the wall")

bottle_verse(99)

for i in range(5, 0, -1):
    bottle_verse(i)
    print()