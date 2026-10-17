import socket
import urllib.parse

HOST = "127.0.0.1"
PORT = 8080

# Demo credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "python123"


def create_response(body, status="200 OK"):
    body = body.encode()

    response = (
        f"HTTP/1.1 {status}\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    ).encode()

    return response + body


def login_page(message=""):
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Python Login Lab</title>

    <style>
        body {{
            font-family: Arial;
            background: #111827;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .box {{
            background: #1f2937;
            padding: 30px;
            border-radius: 10px;
            width: 320px;
        }}

        input {{
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }}

        button {{
            width: 100%;
            padding: 10px;
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }}

        .message {{
            margin-bottom: 15px;
            color: #facc15;
        }}
    </style>
</head>

<body>

<div class="box">

    <h2>Python Login Lab</h2>

    <p class="message">{message}</p>

    <form method="POST" action="/login">

        <input
            type="text"
            name="username"
            placeholder="Username"
        >

        <input
            type="password"
            name="password"
            placeholder="Password"
        >

        <button type="submit">
            Login
        </button>

    </form>

</div>

</body>
</html>
"""


def handle_client(client):

    request = client.recv(4096).decode(errors="ignore")

    if not request:
        return

    print("\n----- REQUEST -----")
    print(request)

    # GET request
    if request.startswith("GET /"):

        response = create_response(
            login_page()
        )

        client.sendall(response)
        return

    # POST request
    if request.startswith("POST /login"):

        # Body comes after blank line
        parts = request.split("\r\n\r\n", 1)

        if len(parts) != 2:
            client.sendall(
                create_response(
                    login_page("Invalid request"),
                    "400 Bad Request"
                )
            )
            return

        body = parts[1]

        # Parse form data
        data = urllib.parse.parse_qs(body)

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        print(f"Username: {username}")
        print(f"Password: {password}")

        # Check credentials
        if (
            username == VALID_USERNAME
            and password == VALID_PASSWORD
        ):

            message = "LOGIN SUCCESSFUL!"

        else:

            message = "Invalid username or password."

        response = create_response(
            login_page(message)
        )

        client.sendall(response)


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))

    server.listen(5)

    print("=" * 50)
    print("Python Socket Login Lab")
    print("=" * 50)

    print(f"Server running at:")
    print(f"http://{HOST}:{PORT}")

    print("\nDemo credentials:")
    print("Username:", VALID_USERNAME)
    print("Password:", VALID_PASSWORD)

    print("\nWaiting for connections...\n")

    while True:

        client, address = server.accept()

        print("Connection from:", address)

        try:
            handle_client(client)

        except Exception as error:
            print("Error:", error)

        finally:
            client.close()


if __name__ == "__main__":
    start_server()