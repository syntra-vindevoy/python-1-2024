import socket
import threading
import time
from queue import Queue

socket.setdefaulttimeout(0.25)

PRINT_LOCK = threading.Lock()
THREAD_COUNT = 100
PORT_START = 1
PORT_END = 500


def scan_port(target_ip, port):
    try:
        resolved_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        with PRINT_LOCK:
            print(f"Error: Cannot resolve IP {target_ip}")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((resolved_ip, port))
            with PRINT_LOCK:
                print(f"Port {port} is open on {resolved_ip}")
        except (socket.timeout, ConnectionRefusedError):
            # Common exceptions for closed/filtered ports, ignore them
            pass
        except Exception as e:
            with PRINT_LOCK:
                print(f"Unexpected error on IP {resolved_ip}, port {port}: {e}")


def start_threads(queue, target_ip):
    def thread_worker():
        while True:
            port = queue.get()
            if port is None:  # End thread signal
                break
            scan_port(target_ip, port)
            queue.task_done()

    threads = []
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    return threads


def scan_ip_range(ip_prefix, host_start, host_end):
    for host in range(host_start, host_end):
        target_ip = f"{ip_prefix}.{host}"
        print(f"Scanning {target_ip}")

        queue = Queue()
        threads = start_threads(queue, target_ip)

        # Add ports to the queue
        for port in range(PORT_START, PORT_END):
            queue.put(port)

        # Indicate the end of the queue for each thread
        for _ in range(THREAD_COUNT):
            queue.put(None)

        # Wait for all tasks to complete
        queue.join()

        # Join threads to finish cleanly
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    start_time = time.time()
    scan_ip_range("10.20.2", 174, 254)
    print('Time taken:', time.time() - start_time)
