import socket
from smtp_router import send_email

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Provider-Aware Mail Server running on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"\nConnection from {addr}")

    try:
        data = conn.recv(4096).decode()

        sender, receiver, subject, body = data.split("|", 3)

        result = send_email(
            sender,
            receiver,
            subject,
            body
        )

        print(result)

        conn.send(result.encode())

    except Exception as e:
        error_message = f"Server Error: {e}"
        print(error_message)
        conn.send(error_message.encode())

    conn.close()
