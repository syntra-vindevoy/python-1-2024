"""Exercise 7.3. The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:
Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi."""
import math

formula_fix = (2 * math.sqrt(2)) / 9801
result = 0
for k in range (0, 2000):
    formula_var = (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
    result += formula_fix * formula_var

print (1 / result)
