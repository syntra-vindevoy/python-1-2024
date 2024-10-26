import math
from Chap_7.sqrt import mysqrt


# Define the function to print the comparison table
def square_root():
    print(f"{'a':<5} {'mysqrt(a)':<15} {'math.sqrt(a)':<15} {'diff':<10}")
    print(f"{'-' * 5} {'-' * 15} {'-' * 15} {'-' * 10}")

    for a in range(1, 10):  # from 1 to 9
        my_result = mysqrt(a)
        math_result = math.sqrt(a)
        difference = abs(my_result - math_result)
        print(f"{a:<5} {my_result:<15.10f} {math_result:<15.10f} {difference:<10.10g}")


# Run the test function
square_root()
