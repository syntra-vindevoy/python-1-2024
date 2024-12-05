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
    midvalue = (lower_limit + upper_limit) / 2
    if given_value == midvalue:
        return lower_limit, upper_limit, given_value, count
    else:
        if given_value < midvalue:
            upper_limit = math.ceil(midvalue)
        elif given_value > midvalue:
            lower_limit = math.floor(midvalue)
        count += 1
        return hint(lower_limit, upper_limit, given_value, count)


def main():
    solutions = []
    max_value = 0
    for i in range(1, 10_001):
        solutions.append(
            hint(
                lower_limit=0,
                upper_limit=10_001,
                given_value=i,
            )
        )
        if solutions[-1][-1] > max_value:
            max_value = solutions[-1][-1]

    pprint(solutions)
    print(max_value)

if __name__ == "__main__":
    main()
