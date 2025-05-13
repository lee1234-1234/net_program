from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print('<- ', data.decode())
    resp = input('-> ')
    sock.sendto(resp.encode(), addr)