import socket
from datetime import datetime

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024


def create_socket() -> None:
    print(f"client is connecting...")
    greeting = f"hi server at:{ datetime.now() }"
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
        # sock.connect((HOST, PORT))
        # sock.sendall(bytes(greeting, "utf-8"))
        sock.sendto(bytes(greeting, "utf-8"), (HOST, PORT))
        pass
    print(f"client disconnected!")
    pass


create_socket()
