from Binary import dec_to_binary_loop

def dec_to_hexadecimal(n):
    if n == 0: return "0"
    binary = int(dec_to_binary_loop(n))
    hexadecimal_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hexadecimal = ""
    while binary > 0:
        temp_binary = binary % 10000
        single_hex = 0
        for i in range (len(str(temp_binary))):
            if temp_binary % 10 == 1: single_hex += 2 ** i
            temp_binary = temp_binary // 10
        hexadecimal = hexadecimal_list[single_hex] + hexadecimal
        binary = binary // 10000
    return hexadecimal
