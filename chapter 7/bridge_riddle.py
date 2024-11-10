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

def bridge_riddle(left, right, time = 0, all_times = [], steps = ""):
    if len(left) == 0:
        all_times.append(time)
        print (f"Time = {time} , Steps : {steps}")
        return

    pairs = split_in_pairs (left)
    for pair in pairs:
        run_time = time
        left_new, right_new = move_left_to_right (left,right,pair)
        run_time += count_time_pair(pair)
        new_steps = steps + f"{pair} cross over, "

        if len(left_new) > 0:
            single = min(right_new) #lets only the fastest person cross
            left_new, right_new = move_right_to_left(left_new,right_new,single)
            run_time += single
            new_steps += f"{single} returns "


        bridge_riddle(left_new, right_new, run_time, all_times, new_steps)


def show_results_bridge_riddle():

    all_times = []
    bridge_riddle([1, 2, 5, 10], [], 0, all_times)
    print (f"The possible results are: {all_times}")
    print (f"The fastest time is {min(all_times)}")

show_results_bridge_riddle()







