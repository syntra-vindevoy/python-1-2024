age = 12
def how_old(int):
    if age < 18:
        return str("Too young")
    elif age <= 18:
        return str("Old enough")
    else:
        return str("Too old")

print(how_old(18))