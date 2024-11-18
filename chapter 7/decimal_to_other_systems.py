from hexadecimal import dec_to_hexadecimal
from Binary import dec_to_binary_loop
from dec_to_roman import higher_roman_numbers

def main (n):
    print (f"Decimal = {n}")
    print (f"Binary = {dec_to_binary_loop(n)}")
    print (f"Hexadecimal = {dec_to_hexadecimal(n)}")
    print (f"Roman = {higher_roman_numbers(n)}")

if __name__ == '__main__':
    main (254255)
