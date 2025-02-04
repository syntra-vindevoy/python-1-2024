words = ["apple", "banana", "cherry", "banana", "date"]
deler = ["cherry", "banana"]
print(words[::-1])
for i in words[::-1]:  # Iterate backwards
    if i in deler:
        words.remove(i)  # Remove "banana"

print(words)  # Output: ['apple', 'cherry', 'date']

words = ["apple", "banana", "cherry", "banana", "date"]

for word in words[:]:  # Iterate over a copy
    if word == "banana":
        words.remove(word)

print(words)  # Output: ['apple', 'cherry', 'date']
