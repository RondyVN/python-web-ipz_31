import socket
from datetime import datetime


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("localhost", 1234)
)

while True:
    message = input(f"[{str(datetime.now())}] ::: ")
    if len(message) > 2048:
        message = "WRONG!! The message is too big"

    client.send(message.encode("utf-8"))
    data = client.recv(2048)
    print(f"[{str(datetime.now())}]", data.decode("utf-8"))

    break