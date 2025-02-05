def cumsum(l:list) -> list:
    new_list = []

    for i in range(len(l)):
        new_list.append(sum(l[:i+1]))

    return new_list

t = [1, 2, 3]
print(cumsum(t))
