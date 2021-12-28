from os import name
import socket
import threading

class gameMember:
  def __init__(self, name = None, port  = None, conn  = None):
    self.name = name
    self.port = port
    self.conn = conn

connections = []
player1=gameMember()
player2=gameMember()

def handleConnection(conn, address):
    # global connections
    print('starting listenning')
    with conn:
        while True:
            data =  conn.recv(1024)
            print('sending massage')
            name=data.decode
            connections.append(gameMember(name, conn, address ))
            if not data:
                break
            conn.send(data)
            # for connection in connections:
            #     # here we handle the client
            #     print('sending ' + bytes(data))
            #     connection.send(bytes(data))

            # if not data:
            #     c.close()
            #     break




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM tcp, for utp SOCK_DGRAM
ip_address = '172.1.0/24' # or 172.1.0.4
ip_address = 'localhost' #TODO change
port=7000
sock.bind((ip_address ,port))
sock.listen(2) # how many connections we allow
print('Server started, listening on IP address ' + ip_address)
while True:
    c, a = sock.accept() #connection, address
    connections.append(c)
    # handleConnection(c, a)
    connectionThread = threading.Thread(target=handleConnection, args=(c,a))
    # connectionThread.daemon = True #let the program get closed
    connectionThread.start()
    connectionThread.run()
    print('excepted connection')
    print(connections)
