import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

command = input("Command (send/list): ")

if command == "send":
    sender = input("From: ")
    receiver = input("To: ")
    subject = input("Subject: ")
    message = input("Message: ")

    full_message = f"send|{sender}|{receiver}|{subject}|{message}"

elif command == "list":
    email = input("Email: ")
    full_message = f"list|{email}"

elif command == "read":
    email = input("Email: ")
    filename = input("Filename: ")
    full_message = f"read|{email}|{filename}"

else:
    full_message = "unknown"

client.send(full_message.encode())

response = client.recv(4096).decode()
print(response)

client.close()
