from itertools import combinations
def weight_40kg_problem():

    weights = [1, 3 , 9, 27, -1, -3, -9, -27]
    all_combinations = []
    all_results = []
    no_doubles = []
    all_positive = []

    for i in range (1, len(weights) + 1):
        all_combinations.extend(list(combinations(weights, i)))

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
    print ("This function checks if any weight from 0 to 40 can be measured using pieces of 1, 3, 9 and 27")
    n = input("Please enter a weight from 0 to 40: ")
    n = int(n)
    if n in possibilities: print (f"{n} is possible")
    else: print (f"{n} is not possible")
try_any_weight()