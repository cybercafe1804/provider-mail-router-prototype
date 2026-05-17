import socket
import os
from dotenv import load_dotenv
from smtp_router import get_smtp_provider

load_dotenv()

HOST = "0.0.0.0"
PORT = 5000

SMTP_MODE = os.getenv("SMTP_MODE", "test")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Provider-Aware Mail Server running on {HOST}:{PORT}")

while True:
    client_socket, address = server.accept()

    data = client_socket.recv(4096).decode()

    if data.lower() == "list":
        files = os.listdir("messages")

        if not files:
            response = "No stored messages found."
        else:
            response = "\n".join(files)

        client_socket.send(response.encode())
        client_socket.close()
        continue

    try:
        from_email, to_email, subject, body = data.split("|")

        filename = f"messages/{subject}.txt"

        with open(filename, "w") as file:
            file.write(f"FROM: {from_email}\n")
            file.write(f"TO: {to_email}\n")
            file.write(f"SUBJECT: {subject}\n")
            file.write(f"MESSAGE: {body}\n")

        provider = get_smtp_provider(to_email)

        response = f"""
TEST MODE - Email not actually sent.

Provider routing decision:
From: {from_email}
To: {to_email}
Provider: {provider['provider']}
SMTP Host: {provider['host']}
Port: {provider['port']}
Subject: {subject}
Message: {body}
"""

        client_socket.send(response.encode())

    except Exception as e:
        error_message = f"Server Error: {str(e)}"
        client_socket.send(error_message.encode())

    client_socket.close()

