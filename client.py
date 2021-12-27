import socket


def getMessage():
    print('Enter your message:')
    myMassage = input()
    return myMassage


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
host='localhost'
port=7000
s.connect((host,port))  #todo if the server is down, will throw exception

for i in range(4):
    message = getMessage()

    message=message.encode()


    s.send(message)
    print('massage sent')
    message= s.recv(1024)

    print('client code here: ')
    print(message)
s.close()