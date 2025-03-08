
import math
def estimate_pi ():
    formula_fix = (2 * math.sqrt(2)) / 9801
    result = 0
    k = 0
    formula_var = (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
    print (formula_var)

    while (formula_fix * formula_var) > 1e-15:
        result += formula_fix * formula_var
        k += 1
        formula_var = (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))

    return result

if __name__ == "__main__":
    print ( f"Approximated Pi = {1 / estimate_pi()}")
    print ( f"Pi from math.pi = {math.pi}")
