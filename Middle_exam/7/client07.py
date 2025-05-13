from socket import *
import time

port = 4321
BUFFSIZE = 1024
RETRY_LIMIT = 3
TIMEOUT = 1  # seconds

sock = socket(AF_INET, SOCK_DGRAM)
sock.settimeout(TIMEOUT)

while True:
    msg = input('Enter a message("send mboxId message" or "receive mboxId"):')
    if msg == 'quit':
        break

    attempts = 0
    while attempts < RETRY_LIMIT:
        sock.sendto(msg.encode(), ('localhost', port))
        try:
            data, addr = sock.recvfrom(BUFFSIZE)
            print(data.decode())
            break
        except timeout:
            attempts += 1

sock.close()