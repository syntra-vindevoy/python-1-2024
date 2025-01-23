def main():
    pos = []
    input_list = [1, 7, 11, 13, 33, 48, 50]
    target = 55
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] + input_list[j] == target:
                pos.append(i)
                pos.append(j)
    print(pos)

def find_pairs(input_list, target):
    indices = {}
    pos = []
    for i, num in enumerate(input_list):
        diff = target - num
        if diff in indices:
            pos.extend([indices[diff], i])
            break
        indices[num] = i
    return pos

def two_sum():
    input_list = [1, 7, 11, 13, 33, 48, 50]
    target = 55
    pos = find_pairs(input_list, target)
    print(pos)


if __name__ == "__main__":
    main()
    print(two_sum())
