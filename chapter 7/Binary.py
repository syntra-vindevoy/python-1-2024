from math import log

def dec_to_binary_loop (n:int) -> str:
    if n < 0 or not isinstance(n, int): return "Decimal number has to be a positive integer"
    if n == 0 : return "0"

    exp = int(log(n, 2)) #calculates the highest binary to start from
    binary_code = ""
    while exp >= 0:
        if n >= 2 ** exp:
            binary= "1"
            n -= 2**exp
        else: binary= "0"

        binary_code += binary
        exp -= 1
    return binary_code


def dec_to_binary_rec (n:int, exp = 2, binary_code = ""):
    if n <= 0 or not isinstance (n, int): return "Decimal number has to be a positive integer"

    if (n % exp) == 0 :
        binary_code = "0" + binary_code

    else:
        binary_code = "1" + binary_code
        n -= (n % exp)
        if n == 0: return binary_code

    return dec_to_binary_rec (n, exp * 2, binary_code)

if __name__ == "__main__":
    assert dec_to_binary_loop(0) == "0"
    assert dec_to_binary_loop(-8) == "Decimal number has to be a positive integer"
    assert dec_to_binary_loop(8.4) == "Decimal number has to be a positive integer"
    assert dec_to_binary_rec(18) == "10010"
    assert dec_to_binary_loop(25) == "11001"
    assert dec_to_binary_rec(-8) == "Decimal number has to be a positive integer"
    assert dec_to_binary_rec(0) == "Decimal number has to be a positive integer"
    assert dec_to_binary_rec(-56) == "Decimal number has to be a positive integer"
    assert dec_to_binary_rec(4.9) == "Decimal number has to be a positive integer"
    
    print (dec_to_binary_loop(8))
    print (dec_to_binary_rec(47))
