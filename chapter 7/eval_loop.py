import math

def eval_loop ():
    x = input ("Give your input (To stop enter 'done'): ")
    while x != "done":
        try:
            eval(x)
            print(f"The result is: {eval(x)}")

        except (ZeroDivisionError, TypeError, NameError, SyntaxError):
            print("No valid input")

        return eval_loop()

eval_loop ()