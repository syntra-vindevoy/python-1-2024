def split_in_pairs (left):
    pairs = []

    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            pairs.append((left[i], left[j]))
    return pairs

def move_left_to_right (left, right, pair):
    right.extend (pair)
    left.remove (pair[0])
    left.remove (pair[1])
    return left, right

def count_time_pair (pair):
    if pair[0] > pair[1]: time = pair[0]
    else: time = pair[1]
    return time

def move_right_to_left (left, right, single):
    left.extend (single)
    right.remove (single)
    return left, right


