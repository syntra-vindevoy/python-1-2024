def nested_sum():
    lijst = [1 ,2, 3,10]
    som = sum(lijst)
    print(som)

nested_sum()



def add_all(t):
    total = 0

    for sublist in t:
        total += sum(sublist)
    return total

t= [1,2,3,[1,2,3]]
print(add_all(t))

#t = [[1, 2], [3], [4, 5, 6]]
#nested_sum(t)
#21