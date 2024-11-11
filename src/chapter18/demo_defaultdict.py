import math
from collections import defaultdict


def main():
    d = defaultdict(list)
    t = d['new key']
    t.append('new value')
    print(d['new key'])

    d = defaultdict(list)
    key = ('into', 'the')
    d[key].append('woods')
    print(d[key])
    x = 5
    y = math.log(x) if x > 0 else float('nan')


def signature(word):
    word = word.lower()
    return ''.join(sorted(word))


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d


if __name__ == '__main__':
    main()
