import socket
import os
import time

HOST = '127.0.0.1'
PORT = 5000

def get_provider(email):
    domain = email.split("@")[1]

    if "gmail" in domain:
        return "gmail"
    elif "yahoo" in domain:
        return "yahoo"
    elif "outlook" in domain:
        return "outlook"
    else:
        return "unknown"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server running...")

while True:
    conn, addr = server.accept()
    data = conn.recv(4096).decode()

    parts = data.split("|")
    command = parts[0]

    if command == "send":
        sender = parts[1]
        receiver = parts[2]
        subject = parts[3]
        message = parts[4]

        provider = get_provider(receiver)

        folder = f"data/{provider}/{receiver}"
        os.makedirs(folder, exist_ok=True)

        filename = f"{int(time.time())}.txt"
        filepath = os.path.join(folder, filename)

        with open(filepath, "w") as f:
            f.write(f"From: {sender}\n")
            f.write(f"To: {receiver}\n")
            f.write(f"Subject: {subject}\n\n")
            f.write(message)

        conn.send(f"Message saved to {filepath}".encode())

    elif command == "list":
        email = parts[1]
        provider = get_provider(email)
        folder = f"data/{provider}/{email}"

        if os.path.exists(folder):
            files = os.listdir(folder)
            conn.send("\n".join(files).encode())
        else:
            conn.send("No inbox found.".encode())

    elif command == "read":
        email = parts[1]
        filename = parts[2]

        provider = get_provider(email)
        filepath = f"data/{provider}/{email}/{filename}"

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                content = f.read()
            conn.send(content.encode())
        else:
            conn.send("Message not found.".encode())

    else:
        conn.send("Unknown command.".encode())

    conn.close()
