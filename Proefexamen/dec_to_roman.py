def dec_to_roman(n:str):
    roman = ["I", "V", "X", "L", "C", "D", "M" ]
    decimals = len (n)
    roman_number = ""
    start = 0
    for i in range(len (n)):
        x = int(n[decimals -1])
        decimals = decimals - 1
        if x == 0: None
        elif x < 4: roman_number = roman[start] * x + roman_number
        elif x == 4: roman_number = roman[start] + roman[start+1] + roman_number
        elif x < 9: roman_number = roman[start+1] + roman[start] * (x-5) + roman_number
        elif x == 9: roman_number = roman[start] + roman[start+2] + roman_number
        start += 2
        print (roman_number)

dec_to_roman("18")

