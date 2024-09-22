import socket
import threading
import sys

def reverse_cipher(text):
    return text[::-1]

def send_message(sock):
    while True:
        message = input("Enter a msg: ")
        cipher_text = reverse_cipher(message)
        print(f"\nPlain text: {message}")
        print(f"Cipher text: {cipher_text}\n")
        sock.send(cipher_text.encode())
        print("Enter a msg: ", end="", flush=True)

def receive_message(sock):
    while True:
        message = sock.recv(1024).decode()
        plain_text = reverse_cipher(message)
        sys.stdout.write("\r" + " " * 50 + "\r") 
        print(f"\nReceived plain text: {plain_text}")
        print(f"Received cipher text: {message}\n")
        print("Enter a msg: ", end="", flush=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.1.12", 12345)
sock.connect(server_address)

send_thread = threading.Thread(target=send_message, args=(sock,))
receive_thread = threading.Thread(target=receive_message, args=(sock,))

send_thread.daemon = True
receive_thread.daemon = True

send_thread.start()
receive_thread.start()

while True:
    pass
