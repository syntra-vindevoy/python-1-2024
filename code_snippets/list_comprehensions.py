square_list = [x**2 for x in range(10)]
square_set = {x**2 for x in range(10)}
square_dict = {x: x**2 for x in range(10)}


# for func in [square_list, square_set, square_dict]:
#    print(func)

[print(func) for func in [square_list, square_set, square_dict]]
