import socket
import threading

HEADER = 16
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.2.27"
#SERVER = "192.168.2.111"
# SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT = "!DISCONNECT"



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send():
    try:
        while True:
            clientChat = input()
            if clientChat == "stop": 
                client.send(DISCONNECT.encode())
                break
            # message = clientChat.encode(FORMAT)
            # message_length = len(message)
            # send_length = str(message_length).encode(FORMAT)
            # send_length += b' ' * (HEADER - len(send_length))
            # client.send(send_length)
            client.send(clientChat.encode())
    except Exception:
        print(Exception)

        
       
    

def receive():
    try:
        while True:
            print(client.recv(1024).decode())
    except Exception:
        print("bye :)")
     


def start():
    print(client.recv(1024).decode())
    name = input(str("Please enter your username : "))
    client.send(name.encode())

    background_receive = threading.Thread(target=receive)
    # background_send = threading.Thread(target=send)
    background_receive.daemon = True
    # background_send.daemon = True
    background_receive.start()
    # background_send.start()
    send()
    client.close()

start()
