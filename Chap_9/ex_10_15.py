from datetime import timedelta, datetime
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


# 10.9

with open("words.txt", "r") as f:
    words = f.read().split()
def method1(words :list[str]):
    lst=[]


    for word in words:
        lst+= [word]

def method2(words :list[str]):
    lst=[]
    for word in words:
        lst.append(word)

def method3(words :list[str]):
    lst = [word for word in words] #[word.upper() for word in sorted(words)]
    return lst

times = 10000
# start = datetime.now()
# for _ in range(times):
#     method1(words)
# end = datetime.now()
# print(f"Time taken: {(end - start).total_seconds()}")

start = datetime.now()
for _ in range(times):
    method2(words)
end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()}")

start = datetime.now()
for _ in range(times):
    method3(words)
end = datetime.now()
print(f"Time taken: {(end - start).total_seconds()}")

#dc = {word: len(word) for word in words}