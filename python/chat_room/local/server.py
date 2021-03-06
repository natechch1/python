import socket
import threading
import sys
import os


HEADER = 16
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"
# create to store all client and used for sending the msg from other client 
list_of_client = {}

SERVER = socket.gethostbyname(socket.gethostname()) # get the IPv4 address
if SERVER.startswith('127.0.'):
    SERVER = '0.0.0.0'
ADDR = (SERVER, PORT)

#create a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR) 



def handle_client(connect, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    connected = True
    while connected:
        message = connect.recv(1024).decode()
        if message:
            if message == DISCONNECT:
                connected = False
            broadcast(message, connect)
            print(f"[{address}] {message}")
    connect.close()      
            
        
def broadcast(msg, conn):
    try:
        if len(list_of_client) > 1:
            for client in list_of_client:
                if client != conn:
                        new_msg = "[" + str(list_of_client.get(conn)) + "] " + msg + "\n"
                        client.send(new_msg.encode())
        if msg == DISCONNECT:
            list_of_client.pop(conn)    

    except BrokenPipeError: 
        # Python flushes standard streams on exit; redirect remaining output 
        # to devnull to avoid another BrokenPipeError at shutdown 
        devnull = os.open(os.devnull, os.O_WRONLY) 
        os.dup2(devnull, sys.stdout.fileno()) 
        sys.exit(1)  # Python exits with error code 1 on EPIPE 
                        


def start():
    server.listen(5)
    print(f"[LISTENING] Server is listening on {SERVER}")
    run = True
    while run:
        try:
            connect, address = server.accept()
            connect.send(f"Welcome to the chat room!\nThere are {threading.activeCount()} user".encode())
        
            # get client name part
            s_name = connect.recv(1024)
            s_name = s_name.decode()
            if s_name not in list_of_client:
                list_of_client[connect] = s_name  # contain all client who join the server
            # threading._start_new_thread(handle_client,(connect,address))
            user_had_connected = "had connected! :)\n"
            broadcast(user_had_connected, connect)
            thread = threading.Thread(target=handle_client, args=(connect, address))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        except Exception as e:
            print("[FAILURE] ",e)
            run = False
   
        
      

print("[STARTING] server is starting.....")
start()

