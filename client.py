import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

command = input("Command (send/list): ")

if command == "send":
    from_email = input("From: ")
    to_email = input("To: ")
    subject = input("Subject: ")
    body = input("Message: ")

    payload = f"{from_email}|{to_email}|{subject}|{body}"
    client.send(payload.encode())

elif command == "list":
    client.send("list".encode())

response = client.recv(4096).decode()
print("\nServer Response:")
print(response)

client.close()
