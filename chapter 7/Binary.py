import math
def dec_to_binary (n):
    highest_exp= int(math.log(n, 2))
    binary_code_string = ""
    exp = highest_exp
    while exp > 0:
        if n >= 2 ** (exp-1):
            binary= "1"
            n -= 2**exp
        else:
            binary= "0"
        binary_code_string = binary_code_string + binary
        exp -= 1
    return binary_code_string

print(dec_to_binary(55546))
