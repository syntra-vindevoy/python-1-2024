def prt_sum_n(number):
    som = 0
    if number > 1:
        for i in range(1,number+1):
            som = som+i
    else:
        som = number
    return som


if __name__ == "__main__":
    assert prt_sum_n(0) == 0
    assert prt_sum_n(1) == 1
    assert prt_sum_n(2) == 3
    assert prt_sum_n(3) == 6
    assert prt_sum_n(4) == 10
    assert prt_sum_n(5) == 15
    assert prt_sum_n(6) == 21

    print(prt_sum_n(5))

