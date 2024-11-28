def nested_sum(numbers):
    sums = 0
    for n in numbers: sums += sum (n)
    return sums

print (nested_sum([[1, 2], [3], [4, 5, 6]]))

def cum_sum(numbers):
    t = list(numbers[:1])
    for i in range(1, len(numbers)):
        t.append(t[i - 1] + numbers[i])
    return t

print (cum_sum ([1,3,4,5]))


def middle (numbers):
    t = numbers[1:-1]
    return t

print (middle ([1,2,3,4,5,6]))

def chop(numbers):
    numbers.remove(numbers[0])
    numbers.remove(numbers[-1])
    return None
print (chop ([1,2,3,4,5]))


def is_sorted(numbers):
    return sorted(numbers) == numbers

print (is_sorted([1,3,4,5]))
print (is_sorted(["a", "d", "c"]))

def has_duplicates(n):
    test = False
    for i in range (len(n)):
        if n[i] in n[:i:]: return True
    return test
print (has_duplicates([1, 2, 3, "g", 4, 5, "a", "g" ]))
