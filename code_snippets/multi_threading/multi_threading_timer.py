from time import sleep
import threading
import sys

# Declare the stop_timer flag
stop_timer = False

def run_something(seconds):
    print("Running something...")
    sleep(seconds)


def run_timer():
    global stop_timer
    count = 0
    while not stop_timer:
        count += 1
        sleep(1)

        print(f"\r{count:02}    ", end="")
        sys.stdout.flush()

def main():
    global stop_timer

    # Create threads for both functions
    thread1 = threading.Thread(target=run_something, args=(5,))
    thread2 = threading.Thread(target=run_timer)

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for run_something to finish
    thread1.join()

    # Stop run_timer by setting a flag
    stop_timer = True

    # Wait for run_timer to finish
    thread2.join()
    print("\nDone running something")

if __name__ == "__main__":
    main()