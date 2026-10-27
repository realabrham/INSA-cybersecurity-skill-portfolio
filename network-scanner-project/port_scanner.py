import socket
import sys
from datetime import datetime

target_host = "127.0.0.1"

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(20, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
