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
