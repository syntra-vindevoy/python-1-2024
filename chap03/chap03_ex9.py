#Exercise 9 - Write a func to calc the faculty of a number

def faculty(*, x: int):
    result = 1

    if x > 0:
        for i in range(x, 1, -1):
            result = result * i

        return result
    else:
        return 0

print(faculty(x = 5))
