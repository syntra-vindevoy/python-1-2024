def dec_to_roman(n: int):
    roman = ["I", "V", "X", "L", "C", "D", "M", "O", "K" ]
    roman_number = ""
    start = 0

    extra = "M" * (n // 1000) #solution for numbers > 3999
    n = str(n % 1000) #only needs to calculate everything beneath 1000
    decimals = len (n)

    for i in range(decimals):

        x = int(n[decimals -1])
        if x == 0: pass
        elif x < 4: roman_number = roman[start] * x + roman_number
        elif x == 4: roman_number = roman[start] + roman[start+1] + roman_number
        elif x < 9: roman_number = roman[start+1] + roman[start] * (x-5) + roman_number
        elif x == 9: roman_number = roman[start] + roman[start+2] + roman_number
        start, decimals = start+2, decimals-1

    return extra + roman_number


def higher_numbers_print (n):
    #This function is to "simplify" the visual of high roman numbers, using only roman numbers
    if n < 2000:
        print( "This is only meant for numbers greater than 2000.")
        return
    n_rest = dec_to_roman(n % 1000)
    times_m = dec_to_roman(n // 1000)
    print(f"{times_m} times M + {n_rest}" if n % 1000 != 0 else f"{times_m} times M")
    return

higher_numbers_print (70521)
