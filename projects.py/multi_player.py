import socket
import threading

SERVER_IP = "172.16.16.169"  # Change to your server IP
PORT = 5555

def receive_messages(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg == "NAME":
                client.send(username.encode())
            else:
                print(msg)
        except:
            break

def send_messages(client):
    while True:
        msg = input()
        client.send(msg.encode())

username = input("Enter your username: ").strip()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
threading.Thread(target=send_messages, args=(client,), daemon=True).start()