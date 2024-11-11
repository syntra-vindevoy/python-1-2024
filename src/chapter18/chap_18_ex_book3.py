def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


"""
Rewrite the body of the function using nested conditional expressions.

This function is not very efficient because it ends up computing the same values over and over. Make it more efficient by memoizing it, as described in 
"""


def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """
    if k == 0:
        return 1

    if n == 0:
        return 0

    return binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)


assert binomial_coeff(5, 3) == 5
assert binomial_coeff(10, 5) == 252
assert binomial_coeff(10, 4) == 210

"""Write a more concise version of this method with a list comprehension or generator expression."""


class Deck:
    def __init__(self, n):
        self.cards = []
        self.n = n

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
