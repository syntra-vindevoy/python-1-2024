def eval_loop():
    while True:
        s = input("What do you want to evaluate?")
        if s == 'done':
            break
        else:
            print(eval(s))


eval_loop()