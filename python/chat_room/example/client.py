import socket
import sys

PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname()) # get the IPv4 address
if SERVER.startswith('127.0.'):
    SERVER = '0.0.0.0'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
name = input(str("Please enter your username : "))
print(" Connected to chat server")
s.send(name.encode())

def receive_and_print():
    for message in iter(lambda: s.recv(1024).decode(), ''):
        print(":", message)
        print("")
import threading
background_thread = threading.Thread(target=receive_and_print)
background_thread.daemon = True
background_thread.start()

while 1:
    s.send(input("Please enter your message: ").encode())
    print("Sent")
    print("")