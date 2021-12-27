import socket


def getMessage():
    print('Enter your message:')
    return input()


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=7000
s.connect((host,port))


message = getMessage()

message=message.encode()


s.send(message)
message= s.recv(1024)

print('Ciphertext: ')
print(message)
s.close()