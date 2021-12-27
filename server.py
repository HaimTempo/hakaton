import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM tcp, for utp SOCK_DGRAM

ip_address = '172.1.0/24' # or 172.1.0.4
ip_address = 'localhost'
port=7000
sock.bind((ip_address ,port))
sock.listen(2) # how many connections we allow
connections = []

def handleConnection(c, a):
    global connections
    while True:
        data =  c.recv(1024)
        for connection in connections:
            # here we handle the client
            connections.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break


print('Server started, listening on IP address ' + ip_address)
while True:
    c, a = sock.accept()
    connectionThread = threading.Thread(target=handleConnection, args=(c,a))
    connectionThread.daemon = True #let the program get closed
    connectionThread.start
    connections.append(c)
    print(connections)