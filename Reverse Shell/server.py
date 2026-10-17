# import socket
# host = "0.0.0.0"
# port = 8000
# server = socket.socket()
# server.settimeout(30)

# try:
#     server.bind((host, port))
#     server.listen(1)


#     print(f"Waiting for connection on {port}")
#     connection, address = server.accept()
#     print("Connected: ", address)


#     while True:
#         try:
#             command = input("root@anmol: ")
#             if command.lower() == "exit":
#                 connection.send(b"exit")
#                 break
#             connection.send(command.encode())
#             output = connection.recv(4096).decode()
#             print(output)
#         except KeyboardInterrupt:
#             connection.send(b"exit")
#             break
#         except Exception as e:
#             print(e)
# finally:
#     try:
#         server.close()
#     except:
#         pass

#     server.close()
#     print("Server is closed")



import socket
import time

host = "0.0.0.0"
port = 8000
server = socket.socket()
server.settimeout(30)

connection = None
try:
    server.bind((host, port))
    server.listen(1)
    print(f"[*] Waiting for connection on {port}")
    connection, address = server.accept()
    print(f"\n[*] Connected: {address}")

    connection.send(b"Connected to server successfully")

    while True:
        try:
            message = input("root@anmol: ")
            if message.lower() == "exit":
                connection.sendall(b"exit")
                print(f"[*] Server Disconnected")
                break
            connection.sendall(message.encode())
            response = connection.recv(4096)
            if not response:
                print("[*] Client Disconnected")
                break
            response = response.decode('utf-8')
            if response == "exit":
                print(f"[*] client closed the connection")
                break
            print(f"Client: {response}")
        except (ConnectionResetError, ConnectionAbortedError):
            print("[-] Connection Lost!")
            break
except KeyboardInterrupt:
    print("[*] Ctrl + C is detected. Server is closing")
    time.sleep(2)
    print("[!] Server is Closed")

finally:
    if connection:
        try:
            connection.sendall(b"exit")
        except:
            pass
        connection.close()
    server.close()