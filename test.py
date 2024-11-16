def balanced_ternary_representation(n):
    result = []
    while n != 0:
        remainder = n % 3
        n = n // 3

        if remainder == 2:
            remainder = -1
            n += 1

        result.append(remainder)

    while len(result) < 4:  # Pad with zeroes for weights up to 40
        result.append(0)

    return result


def calculate_pans(weight):
    balanced_ternary = balanced_ternary_representation(weight)
    left_pan = []
    right_pan = []

    for i, value in enumerate(balanced_ternary):
        if value == 1:
            right_pan.append(3 ** i)
        elif value == -1:
            left_pan.append(3 ** i)

    return left_pan, right_pan


given_weight = 31
left_pan, right_pan = calculate_pans(given_weight)

# Output the result
print(f"To measure {given_weight} grams:")
print(f"Place the following weights on the left pan: {left_pan}")
print(f"Place the following weights on the right pan: {right_pan}")
