from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 4
SERVER_ADDR = ('localhost', 7777)

sock = socket(AF_INET, SOCK_DGRAM)

sock.sendto(b'Hello', SERVER_ADDR)

msg, _ = sock.recvfrom(BUF_SIZE)
if msg != b'Filename':
    print('server:', msg.decode())
    sys.exit()
print('server:', msg.decode())

filename = input('Enter a filename: ')
sock.sendto(filename.encode(), SERVER_ADDR)

msg, _ = sock.recvfrom(BUF_SIZE)
if msg == b'Nofile':
    print('server: No such file')
    sys.exit()

# 파일 크기 수신 (4바이트)
rx_size = len(msg)
data = msg
while rx_size < LENGTH:
    chunk, _ = sock.recvfrom(BUF_SIZE)
    data += chunk
    rx_size += len(chunk)

filesize = int.from_bytes(data, 'big')
print('server: File size =', filesize)

# 파일 수신
rx_size = 0
f = open(filename, 'wb')

while rx_size < filesize:
    data, _ = sock.recvfrom(BUF_SIZE)
    f.write(data)
    rx_size += len(data)

f.close()
print('Download complete')
sock.sendto(b'Bye', SERVER_ADDR)
sock.close()
