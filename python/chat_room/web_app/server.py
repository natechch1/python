from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from  person  import Person

# global constant 
HOST = 'localhost'
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"
# create to store all client and used for sending the msg from other client 
list_of_person = []

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
# if SERVER.startswith('127.0.'):
#     SERVER = '0.0.0.0'


#create a new socket

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
            
        
def broadcast(msg, name):
    for person in list_of_person:
        client = person.client
        client.send("[ " + name + " ] " + msg).encode()
    # try:
    #     if len(list_of_client) > 1:
    #         for client in list_of_client:
    #             if client != conn:
    #                     new_msg = "[" + str(list_of_client.get(conn)) + "] " + msg + "\n"
    #                     client.send(new_msg.encode())
    #     if msg == DISCONNECT:
    #         list_of_client.pop(conn)    

    # except BrokenPipeError as e: 
    #     # Python flushes standard streams on exit; redirect remaining output 
    #     # to devnull to avoid another BrokenPipeError at shutdown 
    #     # devnull = os.open(os.devnull, os.O_WRONLY) 
    #     # os.dup2(devnull, sys.stdout.fileno()) 
    #     # sys.exit(1)  # Python exits with error code 1 on EPIPE 
    #     print("[BROADCAST FAILURE] " + e)
                        

def wait_for_connection():
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            list_of_person.append(person )
            client.send(f"Welcome to the chat room!\nThere are {Thread.activeCount()} user".encode())
            person = Person()
            broadcast("had connected! :)\n", client)
            Thread(target=client_communication, args=(person,)).start()
            print(f"[ACTIVE CONNECTIONS] {Thread.activeCount() - 1}")
        except Exception as e:
            print("[FAILURE] ",e)
            run = False
    print("SERVER CRASHED!")


def client_communication(person):
    client = person.client

    #set the name part
    name = client.receive(1024).decode() 
    broadcast("has joined the chat!" , name)  #broadcast the welcome msg

    while True:
        try:
            msg = person.receive(1024).decode()
            print(f"[ {name} ] " + msg)
            
            if msg == "!quit":
                broadcast(f"{name} has left the chat......", "")  # broadcast the leaving msg
                # client.send(msg).encode()
                client.close
                list_of_person.remove(person)
                break
            else:
                broadcast(msg, name)  # broadcast the normal msg 
        except Exception as e:
            print("[FAILURE] ",e)
            break


        
if __name__ == '__main__':
    SERVER.listen(5)
    print("[STARTING] server is starting.....")
    print(f"[LISTENING] Server is listening on {SERVER}")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close


