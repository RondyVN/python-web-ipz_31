import socket
from datetime import datetime

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    ("localhost", 1234)
)

server.listen(5)
print("Server is listening")

while True:
    user_socket, address = server.accept()
    print(f"[{str(datetime.now())}] User {user_socket} connected!")
    data = user_socket.recv(2048)
    print(f"[{str(datetime.now())}] {address}", data.decode("utf-8"))
