def list_comprehension(fruits):
    return [x for x in fruits if "a" in x]


def list_comprehension2(fruits):
    return [x for x in fruits if x != "apple"]


def list_comprehension3(fruits):
    return [x.upper() for x in fruits]


def list_comprehension4(fruits):
    return [x if x != "banana" else "orange" for x in fruits]


if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    func_list = [list_comprehension, list_comprehension2, list_comprehension3, list_comprehension4]

    for func in func_list:
        print(func(fruits))
    multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]

    print(multiplication)

    # filtering even numbers from a list
    even_numbers = [num for num in range(1, 10) if num % 2 == 0]

    print(even_numbers)

    newlist = [x for x in range(10)]
    print(newlist)

    newlist = [x for x in range(10) if x < 5]

    print(newlist)

    coordinates = [(x, y) for x in range(3) for y in range(3)]

    print(coordinates)

    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    res = [val for row in mat for val in row]

    print(res)

    matrix = [[j for j in range(5)] for i in range(5)]

    print(matrix)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    odd_numbers = [element for row in matrix for element in row if element % 2 != 0]

    print(odd_numbers)

    matrix = [["apple", "banana", "cherry"],
              ["date", "fig", "grape"],
              ["kiwi", "lemon", "mango"]]

    modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]

    print(modified_matrix)

    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]


    def custom_function(a, b):
        return a ** 2 + b ** 2


    result = [custom_function(a, b) for a, b in zip(list_a, list_b)]
    print(result)

    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]

    result = [a + b for a, b in zip(list_a, list_b) if (a + b) % 2 == 0]
    print(result)
