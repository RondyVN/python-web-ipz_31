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
    client.send(input(f"[{str(datetime.now())}] ::: ").encode("utf-8"))