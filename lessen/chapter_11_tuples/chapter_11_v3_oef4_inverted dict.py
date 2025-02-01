def inverted_dict(d):
    temp_dict = dict()
    for key, value in d.items():
        if value not in temp_dict:
            temp_dict[value] = list()
        temp_dict[value].append(key)
    return temp_dict
