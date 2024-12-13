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
    resolved_ip = socket.gethostbyname(target_ip)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((resolved_ip, port))
            with PRINT_LOCK:
                print(f"Port {port} is open")
        except:
            pass


def start_threads(queue, target_ip):
    def thread_worker():
        while True:
            port = queue.get()
            scan_port(target_ip, port)
            queue.task_done()

    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=thread_worker)
        thread.daemon = True
        thread.start()


def scan_ip_range(ip_prefix, host_start, host_end):
    for host in range(host_start, host_end):
        target_ip = f"{ip_prefix}.{host}"
        print(target_ip)
        queue = Queue()
        start_threads(queue, target_ip)

        for port in range(PORT_START, PORT_END):
            queue.put(port)

        queue.join()


if __name__ == '__main__':
    start_time = time.time()
    scan_ip_range("192.168.0", 174, 254)
    print('Time taken:', time.time() - start_time)
