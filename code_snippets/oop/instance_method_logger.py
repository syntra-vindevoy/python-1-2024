import time
import logging
import os

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configure logging to write to a file in the same directory as the executed Python file
log_file = os.path.join(current_dir, 'instance_logger.log')
logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w', format='%(asctime)s - %(message)s')

class CallableTask:
    def __init__(self, param):
        self.param = param

    def __call__(self, method_name):
        method = getattr(self, method_name)
        start_time = time.time()
        logging.info(f"{method_name} called with parameter: {self.param}")
        print(f"{method_name} started with parameter: {self.param}")
        method()
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"{method_name} execution time: {execution_time} seconds")

    def task(self):
        time.sleep(3)
        print("Task done")

    def method1(self):
        time.sleep(1)
        print("Method1 done")

    def method2(self):
        time.sleep(2)
        print("Method2 done")

    def method3(self):
        time.sleep(1.5)
        print("Method3 done")

    def method4(self):
        time.sleep(2.5)
        print("Method4 done")

# Usage
blablabla = CallableTask("Parameter for task")

# Call method4 using the __call__ method
blablabla('method4')