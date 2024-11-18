from sortedcontainers import SortedDict

def main():
    weights = SortedDict()
    stones = [1, 3, 9, 27]

    for stone in stones:
        for p in list(weights.keys()):
            weights[stone + p] = [p, stone]
            weights[stone - p] = [-p, stone]

        weights[stone] = [stone]

    print(weights)

