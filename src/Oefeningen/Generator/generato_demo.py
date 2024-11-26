"""
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of
them in memory at once.


"""


def my_generator(n):
    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1


# iterate over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)

"""
Python Generator Expression
In Python, a generator expression is a concise way to create a generator object.

It is similar to a list comprehension, but instead of creating a list, it creates a generator object that
 can be iterated over to produce the values in the generator.
 (expression for item in iterable)
 """

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)


class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result


def pow_two_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


"""
Represent Infinite Stream
Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

The following generator function can generate all the even numbers (at least in theory).
"""


def all_even():
    n = 0
    while True:
        yield n
        n += 2


"""
Pipelining Generators
Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for
 squaring numbers.

If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way 
by pipelining the output of generator functions together.
"""


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))
