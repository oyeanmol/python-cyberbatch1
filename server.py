# server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Server is Listening...")
client, address = server.accept()
print("Client connected from", address)

while True:
    data = client.recv(1024).decode()
    if data == "exit":
        break
    print("Client: ", data)

    reply = input("You: ")
    reply = reply.encode()
    client.sendall(reply)
    print("Server: ", reply.decode())
client.close()
server.close()



