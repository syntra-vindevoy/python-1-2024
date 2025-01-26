original_dict = dict()


def reset():
    global original_dict
    original_dict = {"zero": 0, "one": 1}


reset()

original_dict["tree"] = 3

dict_copy = dict(original_dict)
dict_copy["tree"] = 33

one_in_dict_keys = "one" in original_dict
one_in_dict_values = 1 in original_dict.values()

for key in original_dict:
    print(key)

for value in original_dict.values():
    print(value)

for key in original_dict:
    print(key, original_dict.value)

some_dict = dict()
for key in original_dict:
    if True:
        some_dict.append(key)


known = {0: 0, 1: 1}


def fibonacci_memo(n):
    if n in known:
        return known[n]
    res = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    known[n] = res
    return res


pass
