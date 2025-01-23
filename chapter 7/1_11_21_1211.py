
def look_and_say(sequence, n):
    for _ in range(n - 1):  # n-1, want de eerste term is al gegeven
        next_sequence = ""
        i = 0

        while i < len(sequence):
            count = 1
            while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
                i += 1
                count += 1
            next_sequence += str(count) + sequence[i]
            i += 1

        sequence = next_sequence

    return sequence

print (look_and_say ("1211", 2))

