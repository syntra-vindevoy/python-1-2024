from stringprep import b1_set


def opp_driehoek(*, h:int, b:int) ->float:
    return (h * b) / 2

#print(opp_driehoek(h=6, b=4))


def opp_vierhoek(*, h:int, b:int) ->float:
    return h * b

#print(opp_vierhoek(h=6, b=4))


def opp(x1:int, x2:int, y1:int, y2:int) -> float:
    b = (x2 - x1)
    h1 = y1
    h2 = (y2 - y1)

    square = opp_vierhoek(h=h1, b=b)
    triangle = opp_driehoek(h=h2, b=b)

    return square + triangle

#print(opp(1, 5, 6, 12))


def parabool(*, x:float) -> float:
    return x**2


def opp_parabool(*, x1:int, x2:int) -> float:
    b1 = x1
    b_step = (x2 - x1) / 128
    area = 0

    while b1 < x2:
        b2 = b1 + b_step
        y1 = parabool(x=b1)
        y2 = parabool(x=b2)
        area += opp(x1=b1, x2=b2, y1=y1, y2=y2)
        b1 += b_step
    return area

print(f"Surface underneath the parabool with function 1: {opp_parabool(x1=0, x2=4)}")



def opp_parabool1(*, x1:int, x2:int) -> float:
    base = 2
    finished = False

    while not finished:
        b1 = x1
        b_step = (x2 - x1) / base
        area = 0

        while b1 < x2:
            b2 = b1 + b_step
            y1 = parabool(x=b1)
            y2 = parabool(x=b2)
            area += opp(x1=b1, x2=b2, y1=y1, y2=y2)
            b1 += b_step
        #return area

        str_area = str(area)
        if '.' in str_area:
            int_part, dec_part = str_area.split('.')
            if len(dec_part) >= 4:
                finished = True
            else:
                base *= 2
        else:
            base *= 2

    return area

print(f"Surface underneath the parabool with function 2: {opp_parabool1(x1=0, x2=4)}")

