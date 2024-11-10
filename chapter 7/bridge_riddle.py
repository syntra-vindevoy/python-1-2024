def split_in_pairs (left):
    pairs = []
    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            pairs.append((left[i], left[j]))
    return pairs

def move_left_to_right (left, right, pair):
    right_new = right.copy()
    left_new = left.copy()
    right_new.extend (pair)
    left_new.remove (pair[0])
    left_new.remove (pair[1])
    return left_new, right_new

def count_time_pair (pair):
    if pair[0] > pair[1]: time_pair = pair[0]
    else: time_pair = pair[1]
    return time_pair

def move_right_to_left (left, right, single):
    left_new = left.copy()
    right_new = right.copy()
    left_new.append (single)
    right_new.remove (single)
    return left_new, right_new

def bridge_riddle(left, right, time = 0, steps = ""):
    if len(left) == 0:
        print (f"Time = {time} , Steps : {steps}")
        return

    pairs = split_in_pairs (left)
    for pair in pairs:
        left_new, right_new = move_left_to_right (left,right,pair)
        run_time = time + count_time_pair(pair)
        new_steps = steps + f"{pair} cross over, "

        if len(left_new) > 0:
            for single in right_new:
                left_temp, right_temp = move_right_to_left(left_new,right_new,single)
                run_time_new = run_time + single
                new_steps_temp = new_steps + f"{single} returns "

                bridge_riddle(left_temp, right_temp, run_time_new, new_steps_temp)
        else:
            bridge_riddle(left_new, right_new, run_time, new_steps)
    return


def show_results_bridge_riddle():

    bridge_riddle([1, 2, 5, 10], [], 0)


show_results_bridge_riddle()







