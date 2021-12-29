from os import name, startfile
import time
import socket
import threading
from gameMember import gameMember
import random

# import gameMember
connections = []
player1=gameMember()
player2=gameMember()
lookForConnection = True
bufferSize = 1024

def handleConnection(conn, address):
    print('server waiting for answer')
    with conn:
        while True:
            data =  conn.recv(bufferSize)
            print('sending massage')
            name=data.decode
            # connections.append(gameMember(name, conn, address ))
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

def assignPlayer(player, clientMsg, clientIP):
    print("clientMsg : "+ clientMsg )
    print("clientMsg : "+ clientIP )
    player.name = clientMsg
    # save player details

def startGame():
    gameStartMassge = "Welcome to Quick Maths.\nPlayer 1: "+ player1.name + "\nPlayer 2: "+ player2.name + "\n==\nPlease answer the following question as fast as you can:\n"
    a = random.randint(0, 9)
    b = random.randint(0, 9 - a)
    gameStartMassge = gameStartMassge + "How much is "+str(a)+" + "+str(b)+"?"
    print("sending to clients: "+ gameStartMassge)
    player1.conn.send(bytes(gameStartMassge))
    player2.conn.send(bytes(gameStartMassge))
    print("need more impliment")
    #wait for plays answers

udpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # SOCK_STREAM tcp, for utp SOCK_DGRAM
# udpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
ip_address = '172.1.0/24' # or 172.1.0.4
ip_address = 'localhost' #TODO change
port=13117
udpServerSocket.bind((ip_address ,port))
# sock.listen(2) # how many connections we allow
print('Server started, listening on IP address ' + ip_address)
while True:
    if lookForConnection:
        bytesAddressPair = udpServerSocket.recvfrom(bufferSize) #accept a new connection
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = str.format(message)
        print("clientMsg "+ clientMsg)
        clientIP  = str.format(address)
        print("clientIP "+ address)
        if (player1.name == None):
            assignPlayer(player1, clientMsg, clientIP)
        elif (player2.name == None):
            assignPlayer(player1, clientMsg, clientIP)
            lookForConnection = False
            startGame()
        else :
            # rejectConnction()
            pass
    time.sleep(1)


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
