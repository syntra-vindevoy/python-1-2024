
def value_counts(sequence: str):
    counts = {}
    for char in sequence:
        counts[char] = counts.get(char, 0) + 1
    return counts

def main():
    print(value_counts('abracadabra'))

if __name__ == "__main__":
    main()