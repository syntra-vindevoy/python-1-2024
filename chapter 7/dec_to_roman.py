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

print (dec_to_roman(662))
