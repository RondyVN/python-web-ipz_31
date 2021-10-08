import threading
import socket

host = "localhost"
port = 1234

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    (host, port)
)

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode("utf-8"))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        user_socket, address = server.accept()
        print(f"User {str(address)} connect")

        user_socket.send("NICK".encode("utf-8"))
        nickname = user_socket.recv(1024).decode("utf -8")
        nicknames.append(nickname)
        clients.append(user_socket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode("utf-8"))
        user_socket.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(user_socket,))
        thread.start()


receive()
