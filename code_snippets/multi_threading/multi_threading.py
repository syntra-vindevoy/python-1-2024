import threading
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time
def task_1(param):
    print(f"Task 1 started with parameter: {param}")
    time.sleep(5)
    print("Task 1 done")

@measure_time
def task_2(param):
    print(f"Task 2 started with parameter: {param}")
    time.sleep(10)
    print("Task 2 done")

@measure_time
def task_3(param):
    print(f"Task 3 started with parameter: {param}")
    time.sleep(3)
    print("Task 3 done")

def main():
    chore_1 = threading.Thread(target=task_1, args=("Parameter for task 1",))
    chore_2 = threading.Thread(target=task_2, args=("Parameter for task 2",))
    chore_3 = threading.Thread(target=task_3, args=("Parameter for task 3",))

    chore_1.start()
    chore_2.start()
    chore_3.start()

    chore_1.join()
    chore_2.join()
    chore_3.join()

    print("All tasks done")

if __name__ == "__main__":
    main()