

def eval_loop ():
    x = input ("Give your input (To stop enter 'done'): ")
    while x != "done":
        try:
            result = eval (x)
            print(f"The result is: {result}")

        except (ZeroDivisionError, TypeError, NameError, SyntaxError):
            print("No valid input")

        return eval_loop()

if __name__ == "__main__":
    eval_loop()