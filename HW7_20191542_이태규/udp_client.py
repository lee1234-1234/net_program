from socket import *

port = 5432
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter a message("send mboxId message" or "receive mboxId"):')
    if msg == 'quit':
        break
    sock.sendto(msg.encode(), ('localhost', port))

    data, addr = sock.recvfrom(BUFFSIZE)
    
    print(data.decode())

sock.close()