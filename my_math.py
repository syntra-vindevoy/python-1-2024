#My own mathematical functions

def factorial(n):
    assert type(n) == int, "This function only accepts int"

    if n < 2:
        return 1

    if n == 2:
        return 2

    return n * factorial(n-1)

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120

failed = False

try:
    assert factorial(1024) == 2**1024
except RecursionError:
    failed = True

assert failed

# failed = False
#
# try:
#     assert factorial("a") == "a"
# except RecursionError:
#     failed = True
#
# assert failed