# exercise 10.1 from book thinkpython

t= [[1,2], [4,5,6], [3]]
def nested_sum(list):
    return sum(sum(sublist) for sublist in list)

print(nested_sum(t))
print (t[2])

# exercise 10.2 from book thinkpython

t2 = [1,2,3]
def cumsum(list2):
    result = []
    current_sum = 0
    for num in list2:
        current_sum += num
        result.append(current_sum)
    return result
print(cumsum(t2))

