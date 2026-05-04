import socket
import os
import time

from smtp_router import route_email  # 👈 NEW (top of file)


HOST = "127.0.0.1"
PORT = 5000


def save_email(recipient, sender, subject, body):
    folder = f"data/{recipient}"
    os.makedirs(folder, exist_ok=True)

    filename = f"{int(time.time())}.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as f:
        f.write(f"From: {sender}\n")
        f.write(f"To: {recipient}\n")
        f.write(f"Subject: {subject}\n\n")
        f.write(body)

    return filename


def list_emails(recipient):
    folder = f"data/{recipient}"
    if not os.path.exists(folder):
        return []

    return os.listdir(folder)


def read_email(recipient, filename):
    filepath = f"data/{recipient}/{filename}"

    if not os.path.exists(filepath):
        return "Message not found."

    with open(filepath, "r") as f:
        return f.read()


def handle_client(conn):
    data = conn.recv(4096).decode()
    parts = data.split("|")

    command = parts[0]

    if command == "send":
        sender = parts[1]
        recipient = parts[2]
        subject = parts[3]
        body = parts[4]

        # 🔥 NEW: Provider-aware routing
        route_email(sender, recipient, subject, body)

        filename = save_email(recipient, sender, subject, body)
        conn.send(f"Message saved as {filename}".encode())

    elif command == "list":
        recipient = parts[1]
        emails = list_emails(recipient)

        response = "\n".join(emails) if emails else "No messages."
        conn.send(response.encode())

    elif command == "read":
        recipient = parts[1]
        filename = parts[2]

        message = read_email(recipient, filename)
        conn.send(message.encode())

    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        handle_client(conn)


if __name__ == "__main__":
    start_server()
