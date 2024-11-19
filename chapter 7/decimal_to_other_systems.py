from hexadecimal import dec_to_hexadecimal
from Binary import dec_to_binary_loop
from dec_to_roman import higher_roman_numbers
from dec_to_roman import dec_to_roman

def main (n):
    print (f"Decimal = {n}")
    print (f"Binary = {dec_to_binary_loop(n)}")
    print (f"Hexadecimal = {dec_to_hexadecimal(n)}")
    print (f"Roman = {higher_roman_numbers(n)}" if n > 3999 else f"Roman = {dec_to_roman(n)}")

if __name__ == '__main__':
    main (4255)
