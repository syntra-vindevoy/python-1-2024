from itertools import zip_longest

number1 = 9620
number2 = 485

def nodify(number):
    return [int(c) for c in str(number)[::-1]]

ll1 = nodify(number1)
ll2 = nodify(number2)


print(ll1)
print(ll2)

zipped = zip_longest(ll1, ll2, [0] * (max(len(ll1), len(ll2)) + 1), fillvalue=0)
reduced = [[sum(z) % 10, sum(z) // 10] for z in zipped]
print(reduced)

for i in range(1, len(reduced)):
    reduced[i][0] = int(reduced[i][0] + reduced[i - 1][1])
    reduced[i - 1][1] = 0
    reduced[i][1] = reduced[i][0] // 10 + reduced[i][1]
    reduced[i][0] = reduced[i][0] % 10

result = [r[0] for r in reduced]
print(result)