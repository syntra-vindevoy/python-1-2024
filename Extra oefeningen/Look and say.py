# Let's manually trace the "Look-and-say" sequence for a few terms.
# The sequence starts as: 1, 11, 21, 1211, 111221, 312211, ...

def look_and_say_sequence(n):
    sequence = ["1"]  # Starting element of the sequence

    # Generate the sequence up to the nth term
    for _ in range(1, n):
        prev_term = sequence[-1]
        next_term = ""

        # Variables to iterate and count characters in the previous term
        count = 1
        length = len(prev_term)

        for i in range(1, length):
            if prev_term[i] == prev_term[i - 1]:
                count += 1  # Increment count if the current digit is the same as the previous
            else:
                next_term += str(count) + prev_term[i - 1]  # Append count and the digit
                count = 1  # Reset count for the new digit

        next_term += str(count) + prev_term[-1]  # Append the last group
        sequence.append(next_term)

    return sequence

# Let's generate the first 6 terms of the sequence
print(look_and_say_sequence(12))
