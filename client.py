import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
host='localhost'
port=7000
s.connect((host,port))  #todo if the server is down, will throw exception

for i in range(4):
    message = input('enter your massage to the server:')
    message=message.encode()
    s.send(message)
    print('massage sent')
    serverAnswer = (s.recv(1024)).decode()
    # work with this
    print('recieved from server :\n' + serverAnswer)
s.close()