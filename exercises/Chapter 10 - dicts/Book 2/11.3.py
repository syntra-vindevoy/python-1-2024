# Exercise 11.3 Memoize the Ackermann function from Exercise 6.2 and see if memoization
# makes it possible to evaluate the function with bigger arguments

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))

def ack(m, n, memo=None):

    if memo is None:
        memo = {}

    # Check if we've already computed ack(m, n) before
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0:
        result = n + 1
    elif n == 0:
        result = ack(m - 1, 1, memo)
    else:
        result = ack(m - 1, ack(m, n - 1, memo), memo)

    # Store the computed result in memo for future calls
    memo[(m, n)] = result
    return result





def main():

    print(ackermann(3, 4))
    print(ack(3, 4))

if __name__ == '__main__':
    main()