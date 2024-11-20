def opp_driehoek (h,b):
    return (h*b) / 2

def opp_vierkant (h,b):
    return h*b

def opp (x1, x2, y1, y2):
    return opp_vierkant (x2 - x1, y1) + opp_driehoek (x2 - x1, y2 - y1)

def parabool (x):
    return x ** 2



