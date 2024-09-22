import socket
import threading
import sys

def reverse_cipher(text):
    return text[::-1]

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        plain_text = reverse_cipher(message)
        sys.stdout.write("\r" + " " * 50 + "\r")
        print(f"\nReceived plain text: {plain_text}")
        print(f"Received cipher text: {message}\n")
        print("Enter a msg: ", end="", flush=True)

def send_message(client_socket):
    while True:
        response = input("Enter a msg: ")
        cipher_text = reverse_cipher(response)
        print(f"\nPlain text: {response}")
        print(f"Cipher text: {cipher_text}\n")
        client_socket.send(cipher_text.encode())
        print("Enter a msg: ", end="", flush=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.1.12", 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print("Server listening for incoming connections...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

client_thread = threading.Thread(target=handle_client, args=(client_socket,))
send_thread = threading.Thread(target=send_message, args=(client_socket,))

client_thread.daemon = True
send_thread.daemon = True

client_thread.start()
send_thread.start()

while True:
    pass
