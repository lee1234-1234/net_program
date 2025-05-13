import socket

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', port))

while True:
    msg = input('Enter a message: ')
    if msg == 'q':
        break
    sock.send(msg.encode())
    data = sock.recv(BUFFSIZE)
    print('Server says: ', data.decode())

sock.close()