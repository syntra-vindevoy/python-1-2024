import socket
import time
from multiprocessing import Pool, Lock

socket.setdefaulttimeout(0.25)

PRINT_LOCK = Lock()
PORT_RANGE = range(1, 500)


def scan_port(target_ip_port):
    target_ip, port = target_ip_port
    resolved_ip = socket.gethostbyname(target_ip)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((resolved_ip, port))
            with PRINT_LOCK:
                print(f"Port {port} is open on {target_ip}")
        except:
            pass


def scan_ip_range(ip_prefix, host_start, host_end):
    targets = [(f"{ip_prefix}.{host}", port) for host in range(host_start, host_end) for port in PORT_RANGE]
    with Pool(processes=4) as pool:  # You can adjust the number of processes
        pool.map(scan_port, targets)


if __name__ == '__main__':
    start_time = time.time()
    scan_ip_range("192.168.0", 150, 254)
    print('Time taken:', time.time() - start_time)
