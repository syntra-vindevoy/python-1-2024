from itertools import combinations

solutions = {}

def solve(left, right, total_time, crossings):
    global solutions

    couples = list(combinations(left, 2))

    b_left, b_right, b_total_time, b_crossings = left.copy(), right.copy(), total_time, crossings.copy()

    for couple in couples.copy():
        left, right, total_time, crossings = b_left.copy(), b_right.copy(), b_total_time, b_crossings.copy()

        right.extend(couple)
        left.remove(couple[0])
        left.remove(couple[1])

        total_time += max(couple)
        crossings.append(
            f"{couple[0]} and {couple[1]} cross the bridge in {max(couple)} seconds.  Left: {left}, Right: {right}.  Total time: {total_time}")

        if len(right) == 4:
            if total_time in solutions:
                solutions[total_time].append(crossings)
            else:
                solutions[total_time] = [crossings]

        else:
            c_left, c_right, c_total_time, c_crossings = left.copy(), right.copy(), total_time, crossings.copy()

            for p in right.copy():
                left, right, total_time, crossings = c_left.copy(), c_right.copy(), c_total_time, c_crossings.copy()

                left.append(p)
                right.remove(p)

                total_time += p
                crossings.append(f"{p} goes back in {p} seconds.  Left: {left}, Right: {right}.  Total time: {total_time}")

                solve(left.copy(), right.copy(), total_time, crossings.copy())


def main():
    global solutions

    left = [1, 2, 5, 10]
    right = []

    solve(left, right, 0, [])

    solutions = dict(sorted(solutions.items(), key=lambda item: item[0]))

    for solution in solutions:
        print("solutions in", solution, "seconds")

        cr_counter = 0
        for crossing in solutions[solution]:
            cr_counter += 1
            print("Cross", cr_counter, ":", crossing)

if __name__ == '__main__':

    main()