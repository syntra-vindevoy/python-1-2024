def is_triangle(a, b, c):
    if (a + b < c or b + c < a or a + c < b):
        print("YES")
    else:
        print("NO")

def check_numbers():
    a = int(input("Side 1?"))
    b = int(input("Side 2?"))
    c = int(input("Side 3?"))
    return is_triangle(a, b, c)

check_numbers()