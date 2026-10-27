import socket
import sys
import threading
from datetime import datetime

# Target definition
target = input("Enter target IP to scan: ") or "127.0.0.1"

print("-" * 60)
print(f"[*] Scanning Target: {target}")
print(f"[*] Time Started: {str(datetime.now())}")
print("-" * 60)

# Function to grab banner
def grab_banner(s):
    try:
        return s.recv(1024).decode().strip()
    except:
        return "No banner available"

# Port scanning function
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        result = s.connect_ex((target, port))
        if result == 0:
            banner = grab_banner(s)
            print(f"[+] Port {port}: OPEN (Service/Banner: {banner})")
        s.close()
    except:
        pass

# Threading implementation for speed
print("[*] Starting multi-threaded reconnaissance scan...")
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()
