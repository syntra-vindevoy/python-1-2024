def fact(n: int, t: int = 1) -> int:
    if n < 2:
        return 1
    return fact(n -1, n * t)


#6 1 6
#5 6 30
#4 30 120
#3 120 360
#2 360 720
#1 720

# telkens het volgende getal * de vorige uitkomst vb: 6*1=6 - 5 * 6 = 30 - 4 * 30 = 120 enz