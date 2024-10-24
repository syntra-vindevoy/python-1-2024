def eval_loop():
    while True:
        i = input("Input: ")  # Gebruik input() in Python 3
        try:
            print(eval(i))
        except (NameError, SyntaxError):
            if i == 'done':
                break
            else:
                print(i)

import math  # Voor het geval je complexe functies wilt evalueren

eval_loop()
