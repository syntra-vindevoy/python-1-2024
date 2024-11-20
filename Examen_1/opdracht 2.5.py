from functools import partial


def opp_driehoek (h,b):
    return (h*b) / 2

def opp_vierkant (h,b):
    return h*b

def opp (x1, x2, y1, y2):
    return opp_vierkant (x2 - x1, y1) + opp_driehoek (x2 - x1, y2 - y1)

def parabool (x):
    return x ** 2

if __name__ == "__main__":
    print (opp(0,4,0,16))
    print (opp(0,2,0,4) + opp(2,4,4,16))

def opp_parabool (x1, x2):
    aantal_decimalen = 0
    n = 1
    while aantal_decimalen < 6:
        total = 0
        dx = (x2 - x1) / n
        x_start = x1
        x_end = dx - x1
        for _ in range (n):
            partial = opp(x_start, x_end, parabool (x_start), parabool (x_end))
            total += partial
            x_start = x_end
            x_end = x_start + dx
        decimalen = total - total // 1
        aantal_decimalen = len(str(decimalen))
        n *= 2
    return total

print (opp_parabool(0,4))
