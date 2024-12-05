import random
from random import Random


def binary_search(sequence, item)->(int,int):
    begin_index = 0
    end_index = len(sequence) - 1
    counter=0
    while begin_index <= end_index:
        midpoint = begin_index + round((end_index - begin_index) / 2)
        midpoint_value = sequence[midpoint]
        counter += 1
        if midpoint_value == item:
            return midpoint, counter
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None



def guess(nbr:int):
    pos, count = binary_search(range(1, 10001), nbr)
    print(f"getal  = {nbr} - positie {pos} - aantal {count}")

def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    print("random")
    guess_int=random.randint(1, 10000)
    guess(guess_int)
    print("ondergrens")
    guess(1)
    print("bovengrens")
    guess(10000)

    print("averga")
    list_count=[]
    for i in range(1,10001):
        _, count = binary_search(range(1, 10001), i)
        list_count.append(count)
    l= range(1,10001)
    print(max([ binary_search(l,i) for i in l]))
    print(min([binary_search(l, i) for i in l]))
    print(f"Average  ={round(calculate_average(list_count))}")


