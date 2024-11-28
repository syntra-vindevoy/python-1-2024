# getal van 1 tot 10_000 random
# laat computer raden welk getal het is
# wat is de langste duur om het juiste getal te vinden?
# werken met ondergrens en bovengrens
# aanpassen met de helft

# aantal stappen
# opletten met grenswaarden en afrondingen


def game(number: int):
    hint(
        0,
        number,
        number,
    )


def hint(lower_limit: int, upper_limit: int, given_value: int, count=0):
    midvalue = (lower_limit + upper_limit) / 2
    if given_value == midvalue:
        return lower_limit, upper_limit
    else:
        if given_value < midvalue:
            upper_limit = midvalue
        elif given_value > midvalue:
            lower_limit = midvalue
        count += 1
        return hint(lower_limit, upper_limit, given_value, count)


def main():
    secret_value = 555
    print(hint())


if __name__ == "__main__":
    main()
