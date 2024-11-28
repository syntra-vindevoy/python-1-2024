def cumsum(numbers):
    cumulative = []
    total = 0
    for num in numbers:
        total += num
        cumulative.append(total)
    return cumulative

# Example usage:
t = [1, 2, 3]
print(cumsum(t))  # Output: [1, 3, 6]
