
'''
__init__ 
This is the constructor method. It is called when an instance of the class is created. It initializes the instance with the given parameters. In this case, it sets the param attribute of the instance.

__call__ 
This method makes an instance of the class callable like a function. When you call the instance (e.g., task()), the __call__ method is executed. In this case, it prints a message, waits for 3 seconds, and then prints another message.

'''


import time

class CallableTask:
    def __init__(self, param):
        self.param = param

    def __call__(self):
        print(f"Task started with parameter: {self.param}")
        time.sleep(3)
        print("Task done")

# Usage
task = CallableTask("Parameter for task")
task()  # This will call the __call__ method