from itertools import combinations

def weight_40kg_problem():

    weights = [1, 3 , 9, 27, -1, -3, -9, -27]
    all_combinations = []
    all_results = []
    no_doubles = []
    all_positive = []
    false_combinations = []

    for i in range (1, len(weights) + 1):
        all_combinations.extend(list(combinations(weights, i)))

    for i in all_combinations: #lists all combinations containing combinations that use the same weight twice
        for j in i:
            if -j in i: false_combinations.append(i)

    for i in false_combinations: #removes all false combinations from list
        if i in all_combinations:
            all_combinations.remove(i)

    for x in all_combinations:
        n = len(x)
        result = 0
        while n > 0:
            result += x[n-1]
            n -= 1
        all_results.append(result)

    for any in all_results:
        if any not in no_doubles: no_doubles.append(any)
    for pos in no_doubles:
        if pos >=0: all_positive.append(pos)

    all_results.sort()
    no_doubles.sort()
    all_positive.sort()

    return all_positive

def try_any_weight():
    possibilities = weight_40kg_problem()
    print ("\nThis function checks if any weight from 0 to 40 can be measured using pieces of 1, 3, 9 and 27")
    n = input("Please enter a weight from 0 to 40: ")
    n = int(n)
    if n in possibilities or n == 0: print (f"{n} is possible")
    else: print (f"{n} is not possible")
try_any_weight()
