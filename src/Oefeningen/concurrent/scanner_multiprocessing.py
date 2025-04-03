import socket
import threading
import time
from queue import Queue

# Set a default timeout for socket connections
socket.setdefaulttimeout(0.25)

# Thread-safe print lock for consistent output
PRINT_LOCK = threading.Lock()

# Tuneable parameters
THREAD_COUNT = 100  # Number of worker threads
PORT_START = 1  # Starting port number to scan (1 for privileged ports)
PORT_END = 500  # Ending port number to scan


def scan_port(target_ip, port):
    """
    Scans a single port on a target IP address.
    """
    try:
        # Resolve the target IP address
        resolved_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        with PRINT_LOCK:
            print(f"Error: Cannot resolve IP {target_ip}")
        return

    try:
        # Create a socket and attempt to connect to the port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((resolved_ip, port))
            with PRINT_LOCK:
                print(f"Port {port} is open on {resolved_ip}")
    except (socket.timeout, ConnectionRefusedError):
        # Ignore if the port is closed or the connection is refused
        pass
    except Exception as e:
        with PRINT_LOCK:
            print(f"Error on IP {resolved_ip}, Port {port}: {e}")


def start_threads(queue, target_ip):
    """
    Starts worker threads for processing ports from the queue.
    Returns a list of threads.
    """

    def thread_worker():
        while True:
            port = queue.get()
            if port is None:  # Exit signal
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
    """
    Scans a range of hosts on a given IP prefix for the specified ports.
    """
    for host in range(host_start, host_end):
        target_ip = f"{ip_prefix}.{host}"
        print(f"Scanning {target_ip}")

        # Queue to manage port assignments
        queue = Queue()
        threads = start_threads(queue, target_ip)

        # Add ports to scan into the queue
        for port in range(PORT_START, PORT_END):
            queue.put(port)

        # Signal threads to terminate
        for _ in range(THREAD_COUNT):
            queue.put(None)

        # Wait for all worker tasks to complete
        queue.join()

        # Ensure all threads cleanly exit
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    start_time = time.time()

    # Scan an example IP range (adjust as needed)
    scan_ip_range("10.20.2", 174, 254)

    # Print time taken for scanning
    print('Time taken:', time.time() - start_time)
