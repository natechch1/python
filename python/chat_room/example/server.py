import socket
import sys

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
SERVER = socket.gethostbyname(host)
s.bind((SERVER,port))
name = input(str("Please enter your username: "))
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print("Recieved connection")
print("")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")

def input_and_send():
    while 1:
        message = name+" : "+input(str("Please enter your message: "))
        conn.send(message.encode())
        print("Sent")
        print("")
import threading
background_thread = threading.Thread(target=input_and_send)
background_thread.daemon = True
background_thread.start()

for message in iter(lambda: conn.recv(1024).decode(), ''):
    print(s_name, ":", message)
    print("")