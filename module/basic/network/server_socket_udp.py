import socket as sk
import time
from concurrent.futures import ThreadPoolExecutor, Future

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024


def hello_from_server(serverSock: sk.socket) -> None:
    data: bytes = serverSock.recv(BUFFER_SIZE)
    print(f"from client: {data.decode('utf-8')}")
    pass


def listen() -> None:
    print(f"server is listening...")
    with sk.socket(family=sk.AF_INET, type=sk.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        # sock.listen()
        with ThreadPoolExecutor(max_workers=5) as clientExecutor:
            # cliSock, addr = sock.accept()
            fut = clientExecutor.submit(hello_from_server, sock)
            fut.result()
            pass
        pass
    print(f"server shutdown!")
    return 1
    pass


def create_socket() -> None:
    print(f"server thread is starting ...")
    with ThreadPoolExecutor(max_workers=1) as serverExecutor:
        fut: Future = serverExecutor.submit(listen)
        fut.result()
        pass
    print(f"server thread is listening ...")
    pass


create_socket()
time.sleep(10.0)
