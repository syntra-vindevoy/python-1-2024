def bridge_riddle():
    left = [1, 2, 5, 10]
    right = []
    combinations_of_two = []

    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            combinations_of_two.append((left[i], left[j]))

    for i in range (6):
        run = combinations_of_two[i]
        left_to_right(run)
        right.extend(run)
        for i in range (len(right)):
            run = right [i]
            right_to_left(run)

        print (left, right)


def left_to_right (run):
    if run[0] > run[1]:
        run_time = run[0]
    else:
        run_time = run[1]
    return run_time

def right_to_left(run):
    run_time = run[0]
    return run_time



bridge_riddle()

