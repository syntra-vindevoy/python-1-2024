def reverse_list(list):
    return list[::-1]

def combine_lists(list1, list2):
    for i in range(len(list1)):
        list1[i] = str(list1[i]) + str(list2[i])
    return list1

def sqaure_in_list(list3):
    for i in range(len(list3)):
        list3[i] = list3[i] ** 2
    return list3

def Concatenate_2_lists(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            result.append(item1 + item2)
    return result

def combine_list(list1, list2):
    list3 = []
    # Iterate through both lists element-wise
    for item1, item2 in zip(list1, reverse_list(list2)):
        result = [item1, item2]  # Combine both results into the final result
        list3.append(result)
    return list3

def remove_emptys(list):
    for i in range(len(list)):
        list.remove("") or list.remove('')
        return list

def add_nr_list(list, nr):
    list[2][2].append(nr)
    return list

def combine_nested_lists(list1, list2):
    list1[2][1][2].extend(list2)
    return list1

def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]


if __name__ == "__main__":
    list1 = [100, 200, 300, 400, 500]
    print(reverse_list(list1))
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    print(combine_lists(list1, list2))
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(sqaure_in_list(numbers))
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    print(Concatenate_2_lists(list1, list2))
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    # print(combine_list(list1, list2))
    resultSet = combine_list(list1, list2)
    for item in resultSet:
        print(item)
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    print(remove_emptys(list1))
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    nr = 7000
    print(add_nr_list(list1, nr))
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    list2 = ["h", "i", "j"]
    print(combine_nested_lists(list1, list2))
    sample_list1 = [1, 2, 5, 4, 5, 6, 5, 8, 9, 10]
    print(remove_value(sample_list1, 5))