import socket
from datetime import datetime
import time

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

    while True:
        data = user_socket.recv(2048)
        time.sleep(5)
        print(f"[{str(datetime.now())}] {address}", data.decode("utf-8"))

        echo = data.decode("utf-8")
        user_socket.send(echo.encode("utf-8"))

        if echo == "stop":
            user_socket.close()
            break



