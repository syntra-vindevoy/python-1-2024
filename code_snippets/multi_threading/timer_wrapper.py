import threading
import sys
from time import sleep

stop_timer = False

def run_timer():
    global stop_timer
    count = 0
    while not stop_timer:
        hours, remainder = divmod(count, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_format = f"\rruntime {hours:02}h:{minutes:02}m:{seconds:02}s"
        print(time_format, end="")
        sys.stdout.flush()
        count += 1
        sleep(1)

def timer(func):
    def wrapper(*args, **kwargs):
        global stop_timer
        stop_timer = False
        timer_thread = threading.Thread(target=run_timer)
        timer_thread.start()
        result = func(*args, **kwargs)
        stop_timer = True
        timer_thread.join()
        return result
    return wrapper

@timer
def run_something(duration):
    sleep(duration)

def main():
    run_something(5)
    print("\nDone running something")

if __name__ == "__main__":
    main()