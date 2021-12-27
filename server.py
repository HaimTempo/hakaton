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
    print('starting listenning')
    with c:
        while True:
            data =  c.recv(1024)
            print('sending massage')
            if not data:
                break
            c.send(data)
            # for connection in connections:
            #     # here we handle the client
            #     print('sending ' + bytes(data))
            #     connection.send(bytes(data))
            
            # if not data:
            #     c.close()
            #     break


print('Server started, listening on IP address ' + ip_address)
while True:
    c, a = sock.accept()
    connections.append(c)
    # handleConnection(c, a)
    connectionThread = threading.Thread(target=handleConnection, args=(c,a))
    # connectionThread.daemon = True #let the program get closed
    connectionThread.start()
    connectionThread.run()
    print('excepted connection')
    print(connections)