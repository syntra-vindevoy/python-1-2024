# getal van 1 tot 10_000 random
# laat computer raden welk getal het is
# wat is de langste duur om het juiste getal te vinden?
# werken met ondergrens en bovengrens
# aanpassen met de helft

# aantal stappen
# opletten met grenswaarden en afrondingen


import math
from pprint import pprint
import random


def game(number: int):
    hint(
        0,
        number,
        number,
    )


def hint(lower_limit: int, upper_limit: int, given_value: int, count: int = 0):
    random_value = random.randint(lower_limit, upper_limit)
    if given_value == random_value:
        return count
    else:
        if given_value < random_value:
            upper_limit = math.ceil(random_value)
        elif given_value > random_value:
            lower_limit = math.floor(random_value)
        count += 1
        return hint(lower_limit, upper_limit, given_value, count)


def main():
    solutions = []
    for i in range(100_000):
        solutions.append(
            hint(
                lower_limit=0,
                upper_limit=10_000,
                given_value=random.randint(0, 10_000),
            )
        )
    pprint(solutions)
    pprint(f"gemiddeld: {sum(solutions)/len(solutions)}")


if __name__ == "__main__":
    main()
