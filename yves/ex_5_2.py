import time
from datetime import datetime


def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n:
        raise Exception("Holy smokes, Fermat was wrong")


if __name__ == "__main__":
    start = time.perf_counter()

    for a in range(1, 51):
        for b in range(1, 51):
            for c in range(1, 51):
                for n in range(3, 60):
                    check_fermat(a, b, c, n)

    end = time.perf_counter()

    print(f"Time taken: {end - start}")


if __name__ == "__main__":
    start = time.perf_counter()

    for a in range(1, 51):
        for b in range(1, 51):
            for c in range(1, 51):
                for n in range(3, 60):
                    if a ** n + b ** n == c ** n:
                        raise Exception("Fermat was wrong")

    end = time.perf_counter()

    print(f"Time taken: {end - start}")


