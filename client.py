# client.py

import socket

Host = "127.0.0.1"
Port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, Port))

while True:
    message = input("You: ")
    client.sendall(message.encode())

    if message == "exit":
        break
    reply = client.recv(1024).decode()
    print("Server: ", reply)

client.close()
