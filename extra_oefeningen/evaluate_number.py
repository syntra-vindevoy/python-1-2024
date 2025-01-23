def evaluate_number(number:int, loops:int):
    if len(str(number)) > 1:
        return "Decimal number has to be a single integer"
    for i in range(1, loops+1):
        print(i)



evaluate_number(10,3)