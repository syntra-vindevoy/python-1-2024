from datetime import timedelta
import random

t = [[1, 2], [3], [4, 5, 6]]
total_sum = 0

for i in t:
    for j in i:
        total_sum += j  # Add each element to the total sum

print("Total sum:", total_sum)

def cumsum(numbers):
    cumulative_sum = []
    total = 0
    for number in numbers:
        total += number
        cumulative_sum.append(total)
    return cumulative_sum

# Example usage:
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = cumsum(z)
print("Cumulative sum:", result)


def middle(numbers):
    return numbers[1:-1]

t = [1, 2, 3, 4, 5]
result1 = middle(t)
print("middle:", result1)

a, b, c, d, e = 1, 2, 3, 4, 5
#a = [1, 2, 3, 4, 5]
a = [a, b, d, c, e]
# Here, sorted(), sort list in ascending order
print(a == sorted(a))

def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

numbers = [1, 2, 3, 4, 5, 1]
print(has_duplicates(numbers))

def has_duplicate_birthdays(birthdays):
    """Check if there is any duplicate birthday in the list."""
    return len(birthdays) != len(set(birthdays))


def estimate_probability(num_students, num_simulations=10000):
    """Estimate the probability of at least two people having the same birthday."""
    duplicate_count = 0

    for _ in range(num_simulations):
        # Generate random birthdays for the specified number of students
        birthdays = [random.randint(1, 365) for _ in range(num_students)]

        # Check for duplicate birthdays
        if has_duplicate_birthdays(birthdays):
            duplicate_count += 1

    # The probability is the fraction of simulations where a duplicate was found
    return duplicate_count / num_simulations


# Estimate the probability for 23 students
probability = estimate_probability(23)
print(f"Estimated probability of at least two students sharing a birthday: {probability:.4f}")


